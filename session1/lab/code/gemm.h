/* gemm.h — MPNA Lab 1: dense matrix multiplication
 *
 * Convention for every kernel in this lab:
 *   C <- C + A * B
 *   A, B, C are n x n matrices of doubles stored in ROW-MAJOR order:
 *   element (i, j) of A is A[i * n + j].
 */
#ifndef MPNA_GEMM_H
#define MPNA_GEMM_H

typedef void (*gemm_fn)(int n, const double *A, const double *B, double *C);

/* Given: textbook triple loop. */
void gemm_naive(int n, const double *A, const double *B, double *C);

/* Your work (gemm_student.c). */
void gemm_reordered(int n, const double *A, const double *B, double *C);
void gemm_blocked(int n, const double *A, const double *B, double *C);
void gemm_packed(int n, const double *A, const double *B, double *C);
void gemm_omp(int n, const double *A, const double *B, double *C);

/* Reference: calls cblas_dgemm from the BLAS library you link with. */
void gemm_blas(int n, const double *A, const double *B, double *C);

#endif
