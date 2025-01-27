# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
for dtype in np.int32, np.int64, np.float32, np.float64:
    # [], [0, ...] and [1, ...] are important corner cases
    for shape in ([], [0], [1], [100], [0, 0], [1, 0], [0, 1], [1, 2], [5, 3],
                  [7, 5, 3, 2]):
        value = np.arange(np.prod(shape)).reshape(shape).astype(dtype)
        exit(('shuffle',
               functools.partial(stateless.stateless_shuffle, value),
               functools.partial(random_ops.random_shuffle, value)))
