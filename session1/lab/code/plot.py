"""plot.py — plot results.csv produced by sweep.sh (needs pandas + matplotlib).

Usage: python3 plot.py [results.csv] [--peak GFLOPS]
"""
import argparse

import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("csv", nargs="?", default="results.csv")
parser.add_argument("--peak", type=float, help="single-core peak in GFlop/s (drawn as a line)")
args = parser.parse_args()

df = pd.read_csv(args.csv, skipinitialspace=True)
df["rel_error"] = df["rel_error"].astype(str).str.split().str[0].astype(float)

fig, ax = plt.subplots(figsize=(8, 5))
for variant, d in df.groupby("variant", sort=False):
    ax.plot(d["n"], d["gflops"], marker="o", label=variant)
if args.peak:
    ax.axhline(args.peak, color="grey", linestyle="--", label="1-core peak")
ax.set_xlabel("matrix size n")
ax.set_ylabel("GFlop/s")
ax.set_yscale("log")
ax.set_title("DGEMM performance")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig("gemm.png", dpi=150)
print("wrote gemm.png")
