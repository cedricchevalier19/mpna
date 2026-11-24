# MPNA lab environment: one image for every lab (see ../compose.yaml).
#
#   C11 + OpenMP (gcc), make, OpenBLAS (BLAS, CBLAS, LAPACK), METIS (Lab 3),
#   Open MPI (project), Python 3 with NumPy, SciPy, matplotlib, pandas.
#
# Build it natively (no --platform): the labs compile with -march=native and
# measure performance, so an emulated image would give meaningless numbers.

FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential make \
      libopenblas-dev \
      metis \
      openmpi-bin libopenmpi-dev \
      python3 python3-numpy python3-scipy python3-matplotlib python3-pandas \
      ca-certificates less nano vim-tiny \
 && rm -rf /var/lib/apt/lists/*

# Plots are written to files; matplotlib needs a writable cache directory
# whatever the user id the container runs with.
ENV MPLBACKEND=Agg \
    MPLCONFIGDIR=/tmp/matplotlib \
    PYTHONDONTWRITEBYTECODE=1 \
    OMPI_MCA_btl_vader_single_copy_mechanism=none

# The repository is mounted at /mpna by compose.yaml.
WORKDIR /mpna
USER ubuntu
CMD ["bash"]
