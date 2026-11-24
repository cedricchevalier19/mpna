/* gemm_naive.c — given code. Do not modify; use it as the baseline. */
#include <cblas.h>
#include "gemm.h"

void gemm_naive(int n, const double *A, const double *B, double *C)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            double cij = C[i * n + j];
            for (int k = 0; k < n; k++)
                cij += A[i * n + k] * B[k * n + j];   /* B is walked down a column */
            C[i * n + j] = cij;
        }
}

void gemm_blas(int n, const double *A, const double *B, double *C)
{
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans,
                n, n, n, 1.0, A, n, B, n, 1.0, C, n);
}
