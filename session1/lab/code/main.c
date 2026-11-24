/* main.c — timing and correctness harness for MPNA Lab 1.
 *
 * Usage: ./gemm <variant> <n> [repetitions]
 *   variant: naive | reordered | blocked | packed | omp | blas | all
 * Output (one CSV line per variant): variant,n,time_s,gflops,rel_error
 */
#define _POSIX_C_SOURCE 200809L
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "gemm.h"

int not_implemented = 0;

static const struct { const char *name; gemm_fn fn; } variants[] = {
    {"naive", gemm_naive},     {"reordered", gemm_reordered},
    {"blocked", gemm_blocked}, {"packed", gemm_packed},
    {"omp", gemm_omp},         {"blas", gemm_blas},
};
#define NVARIANTS (int)(sizeof variants / sizeof variants[0])

static double now(void)
{
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return (double)t.tv_sec + 1e-9 * (double)t.tv_nsec;
}

static double *alloc_matrix(int n)
{
    void *p = NULL;
    /* 64-byte alignment = one cache line, also good for AVX-512 loads */
    if (posix_memalign(&p, 64, (size_t)n * n * sizeof(double)) != 0) {
        perror("posix_memalign");
        exit(EXIT_FAILURE);
    }
    return p;
}

static void fill_random(int n, double *M)
{
    for (size_t i = 0; i < (size_t)n * n; i++)
        M[i] = 2.0 * rand() / RAND_MAX - 1.0;
}

/* ||X - Y||_F / ||Y||_F */
static double rel_error(int n, const double *X, const double *Y)
{
    double num = 0.0, den = 0.0;
    for (size_t i = 0; i < (size_t)n * n; i++) {
        double d = X[i] - Y[i];
        num += d * d;
        den += Y[i] * Y[i];
    }
    return sqrt(num / den);
}

static void run(int v, int n, int reps, const double *A, const double *B,
                const double *C0, const double *Cref, double *C)
{
    double best = INFINITY;
    for (int r = 0; r < reps; r++) {
        memcpy(C, C0, (size_t)n * n * sizeof(double));
        not_implemented = 0;
        double t0 = now();
        variants[v].fn(n, A, B, C);
        double t = now() - t0;
        if (not_implemented) {
            fprintf(stderr, "%s: not implemented yet, skipped\n", variants[v].name);
            return;
        }
        if (t < best) best = t;
    }
    double gflops = 2.0 * n * (double)n * n / best * 1e-9;
    double err = Cref ? rel_error(n, C, Cref) : 0.0;
    printf("%s,%d,%.6f,%.3f,%.2e%s\n", variants[v].name, n, best, gflops, err,
           err > 1e-12 ? "  <-- WRONG RESULT?" : "");
}

int main(int argc, char **argv)
{
    if (argc < 3) {
        fprintf(stderr, "usage: %s <variant|all> <n> [repetitions]\n", argv[0]);
        return EXIT_FAILURE;
    }
    const char *which = argv[1];
    int n = atoi(argv[2]);
    int reps = argc > 3 ? atoi(argv[3]) : 3;
    if (n <= 0 || reps <= 0) {
        fprintf(stderr, "n and repetitions must be positive\n");
        return EXIT_FAILURE;
    }

    double *A = alloc_matrix(n), *B = alloc_matrix(n), *C0 = alloc_matrix(n);
    double *Cref = alloc_matrix(n), *C = alloc_matrix(n);
    srand(42);
    fill_random(n, A);
    fill_random(n, B);
    fill_random(n, C0);

    /* Reference result computed with BLAS */
    memcpy(Cref, C0, (size_t)n * n * sizeof(double));
    gemm_blas(n, A, B, Cref);

    int found = 0;
    for (int v = 0; v < NVARIANTS; v++)
        if (!strcmp(which, "all") || !strcmp(which, variants[v].name)) {
            found = 1;
            run(v, n, reps, A, B, C0, Cref, C);
        }
    if (!found) {
        fprintf(stderr, "unknown variant '%s'\n", which);
        return EXIT_FAILURE;
    }

    free(A); free(B); free(C0); free(Cref); free(C);
    return EXIT_SUCCESS;
}
