# MPNA labs in Docker

One image has everything the labs need: gcc with OpenMP, make, OpenBLAS (BLAS,
CBLAS and LAPACK), METIS (`gpmetis`, Lab 3), Open MPI (project) and Python 3
with NumPy, SciPy, matplotlib and pandas. `compose.yaml`, at the root of the
repository, has one service per lab. Each one opens in that lab's folder.

```sh
docker compose build                  # once, from the repository root
docker compose run --rm lab1          # a shell in session1/lab/code
```

Then follow the lab's README as usual (`make`, `./gemm all 1024`, ...). The
repository is mounted at `/mpna`: you edit your files on your machine with your
own editor, and the results (`*.csv`, `*.png`) appear in the lab folder.

| Service | Folder |
|---|---|
| `lab1` | `session1/lab/code` |
| `lab2` | `session2/lab/code` |
| `lab3-eigen`, `lab3-graph` | `session3/lab/eigen`, `session3/lab/graph` |
| `lab4-dense`, `lab4-qr` | `session4/lab/dense`, `session4/lab/qr` |
| `lab5` ... `lab9` | `session5/lab/code` ... `session9/lab/code` |
| `project` | repository root (`mpicc`, `mpirun` available) |

One command without opening a shell:

```sh
docker compose run --rm lab2 sh -c 'make && ./spmv poisson2d:1000'
```

## Notes

- **Whole repository.** Labs 3 and 5 to 8 compile your code from earlier labs
  (`session2/lab/code/sparse_student.c`, ...). That is why every service mounts
  the whole repository, not only its lab folder.
- **File owner (Linux).** The container writes files as user 1000. If `id -u`
  is not 1000, run `export MPNA_UID=$(id -u) MPNA_GID=$(id -g)` first, or put
  both lines in a `.env` file at the root. Docker Desktop (macOS, Windows)
  does not need this.
- **Native image only.** The labs compile with `-march=native`. Build the image
  for your own machine (no `--platform`). An emulated image (amd64 on an
  Apple Silicon Mac) runs, but many times slower.
- **Performance.** Docker Desktop runs Linux in a virtual machine. The machine
  is the one you measure, but the number of cores and the memory are the ones
  given to that virtual machine (Docker Desktop settings). Measure the peak and
  the bandwidth inside the container, as the labs ask. The numbers that count
  for the project are the ones from the cluster.
- **Network.** Lab 9 downloads MNIST into `session9/lab/code/data` the first
  time. Matrix Market files (`*.mtx`, Labs 2 and 3) are downloaded by you into
  the lab folder.
