# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/data_format_ops_test.py
for dtype in {np.int32, np.int64}:
    x = np.array([9, 3], dtype=dtype)
    self._runPermuteAndCompare(x, "NCHW", "NHWC", [9, 3])
