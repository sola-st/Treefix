# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_stitch_test.py
val1 = np.array([0, 4, 7], dtype=np.int32)
val2 = np.array([1, 6], dtype=np.int32)
val3 = np.array([2, 3, 5], dtype=np.int32)
val4 = np.array([[0, 1], [40, 41], [70, 71]], dtype=np.float32)
val5 = np.array([[10, 11], [60, 61]], dtype=np.float32)
val6 = np.array([[20, 21], [30, 31], [50, 51]], dtype=np.float32)
expected = np.array(
    [[0, 1], [10, 11], [20, 21], [30, 31], [40, 41], [50, 51], [60, 61],
     [70, 71]],
    dtype=np.float32)
self._AssertDynamicStitchResultIs(
    [val1, val2, val3], [val4, val5, val6], expected=expected)
