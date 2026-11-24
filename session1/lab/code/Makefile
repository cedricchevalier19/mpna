# MPNA Lab 1 — build the GEMM harness
#
#   make                  build ./gemm with OpenBLAS
#   make BLAS="-lmkl_rt"  use another BLAS (check `module avail` on the cluster)
#   make clean
#
# Tip: print what the compiler vectorized with  make CFLAGS_EXTRA=-fopt-info-vec

CC      ?= gcc
CFLAGS  = -O3 -march=native -fopenmp -std=c11 -Wall -Wextra $(CFLAGS_EXTRA)
BLAS    ?= -lopenblas
LDLIBS  = $(BLAS) -lm

STUDENT ?= gemm_student.c
OBJS = main.o gemm_naive.o student.o

gemm: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LDLIBS)

%.o: %.c gemm.h
	$(CC) $(CFLAGS) -c $<

student.o: $(STUDENT) gemm.h
	$(CC) $(CFLAGS) -I. -c $(STUDENT) -o $@

clean:
	rm -f gemm $(OBJS)

.PHONY: clean
