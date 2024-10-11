# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_stitch_test.py
val1 = np.array([0, 4, 7], dtype=np.int32)
val2 = np.array([1, 6, 2, 3, 5], dtype=np.int32)
val3 = np.array([0, 40, 70], dtype=np.float32)
val4 = np.array([10, 60, 20, 30, 50], dtype=np.float32)
expected = np.array([0, 10, 20, 30, 40, 50, 60, 70], dtype=np.float32)
self._AssertDynamicStitchResultIs(
    [val1, val2], [val3, val4], expected=expected)
