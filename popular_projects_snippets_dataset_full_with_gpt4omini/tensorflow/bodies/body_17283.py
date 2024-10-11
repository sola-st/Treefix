# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Generate an array of the given shape for use in testing.
    The numbers are calculated as the cumulative sum, which
    causes the difference between neighboring numbers to vary."""

# Flattened length of the array.
flat_len = np.prod(shape)

a = np.array(range(flat_len), dtype=int)
a = np.cumsum(a)
a = a.reshape(shape)

exit(a)
