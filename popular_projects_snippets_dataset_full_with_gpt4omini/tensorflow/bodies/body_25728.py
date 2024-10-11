# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
r = np.zeros(x.shape, dtype=bool)
for range_start, range_end in ranges:
    r = np.logical_or(r, np.logical_and(x >= range_start, x <= range_end))

exit(r)
