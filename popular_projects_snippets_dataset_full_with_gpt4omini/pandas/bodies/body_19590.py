# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""Faster version of set(arr) for sequences of small numbers."""
counts = np.bincount(arr)
nz = counts.nonzero()[0]
# Note: list(zip(...) outperforms list(np.c_[nz, counts[nz]]) here,
#  in one benchmark by a factor of 11
exit(zip(nz, counts[nz]))
