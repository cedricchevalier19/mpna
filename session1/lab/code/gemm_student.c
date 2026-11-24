/* gemm_student.c — your implementations.
 *
 * Each function must compute C <- C + A * B (row-major, n x n).
 * A function is considered "not implemented" while its NOT_IMPLEMENTED
 * marker is present: main.c then skips it. Remove the marker once you
 * have written the function.
 */
#include <stdlib.h>
#include "gemm.h"

#define NOT_IMPLEMENTED(name) do { (void)n; (void)A; (void)B; (void)C; \
    extern int not_implemented; not_implemented = 1; return; } while (0)

/* Step 2 — Loop reordering.
 * Change the loop order so that the innermost loop walks memory
 * contiguously in B and C (hint: i-k-j). */
void gemm_reordered(int n, const double *A, const double *B, double *C)
{
    NOT_IMPLEMENTED(gemm_reordered);
}

/* Step 3 — Cache blocking.
 * Split the three loops into blocks of size BS so that three BS x BS
 * blocks fit in cache. Choose BS experimentally (try 32, 64, 128...).
 * Do not forget the edges when n is not a multiple of BS. */
#ifndef BS
#define BS 64
#endif
void gemm_blocked(int n, const double *A, const double *B, double *C)
{
    NOT_IMPLEMENTED(gemm_blocked);
}

/* Step 4 — Packing + micro-kernel (BLIS / GotoBLAS approach).
 * Loops (outer to inner): jc (NC) -> pc (KC) -> ic (MC) -> jr (NR) -> ir (MR)
 *  - pack a KC x NC panel of B into contiguous NR-wide slivers (fits in L3)
 *  - pack an MC x KC block of A into contiguous MR-tall slivers (fits in L2)
 *  - micro-kernel: update an MR x NR block of C held in registers,
 *    looping over KC (rank-1 updates).
 * Start with MR = 4, NR = 8 (AVX2: NR = 2 vectors of 4 doubles). */
void gemm_packed(int n, const double *A, const double *B, double *C)
{
    NOT_IMPLEMENTED(gemm_packed);
}

/* Step 5 — OpenMP.
 * Parallelize your best version. Which loop should be parallel?
 * (Hint: never one that makes two threads write the same block of C.) */
void gemm_omp(int n, const double *A, const double *B, double *C)
{
    NOT_IMPLEMENTED(gemm_omp);
}
