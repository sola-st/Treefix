# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# TODO(touts): Figure out why the padding tests do not work on GPU
# for int types and rank > 2.
for t in [np.int8, np.uint8, np.int32, np.int64]:
    self._testAll(
        np.random.randint(-100, 100, (4, 4, 3)).astype(t),
        [[1, 0], [2, 3], [0, 2]], 0)
    self._testAll(
        np.random.randint(-100, 100, (4, 2, 1, 3)).astype(t),
        [[0, 0], [0, 0], [0, 0], [0, 0]], -123)
