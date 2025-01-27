# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_stitch_test.py
idx1 = np.array([0, 2], dtype=np.int32)
idx2 = np.array([[1], [3]], dtype=np.int32)
val1 = np.array([[], []], dtype=np.int32)
val2 = np.array([[[]], [[]]], dtype=np.int32)
self._AssertDynamicStitchResultIs(
    [idx1, idx2], [val1, val2],
    expected=np.array([[], [], [], []], np.int32))
