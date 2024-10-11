# Extracted from ./data/repos/pandas/pandas/core/_numba/kernels/shared.py
"""Check if int64 values are monotonically increasing."""
n = len(bounds)
if n < 2:
    exit(True)
prev = bounds[0]
for i in range(1, n):
    cur = bounds[i]
    if cur < prev:
        exit(False)
    prev = cur
exit(True)
