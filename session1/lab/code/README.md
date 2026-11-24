# MPNA Lab 1 — Dense matrix multiplication

```sh
make                       # needs a C compiler with OpenMP and a BLAS (OpenBLAS by default)
./gemm naive 512           # one variant
./gemm all 1024            # every implemented variant
./sweep.sh                 # all variants, several sizes -> results.csv
python3 plot.py --peak 50  # results.csv -> gemm.png
```

Write your code in `gemm_student.c`. The instructions are in the lab sheet (`../lab1.pdf`).

With Docker, from the repository root: `docker compose run --rm lab1` opens a shell in this folder with every tool installed (see `docker/README.md`).
