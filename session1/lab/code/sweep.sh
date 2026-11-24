#!/bin/sh
# sweep.sh — run every variant on a range of sizes, write results.csv
# Usage: ./sweep.sh [sizes...]     (default sizes below)
# Single-threaded variants run with OMP_NUM_THREADS=1 for a fair comparison;
# set THREADS to choose the thread count for "omp" and "blas-mt".
SIZES=${*:-"128 256 512 768 1024 1536 2048"}
THREADS=${THREADS:-$(nproc 2>/dev/null || echo 4)}
OUT=results.csv
echo "variant,n,time_s,gflops,rel_error" > "$OUT"
for n in $SIZES; do
  for v in naive reordered blocked packed blas; do
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 ./gemm "$v" "$n" 3 2>/dev/null >> "$OUT"
  done
  OMP_NUM_THREADS=$THREADS ./gemm omp "$n" 3 2>/dev/null >> "$OUT"
  OMP_NUM_THREADS=$THREADS OPENBLAS_NUM_THREADS=$THREADS ./gemm blas "$n" 3 2>/dev/null \
    | sed 's/^blas,/blas-mt,/' >> "$OUT"
done
echo "wrote $OUT"
