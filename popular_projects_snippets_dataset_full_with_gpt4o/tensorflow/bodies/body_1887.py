# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_stitch_test.py
idx1 = np.array([], dtype=np.int32)
idx2 = np.array([[], []], dtype=np.int32)
val1 = np.ndarray(shape=(0, 9), dtype=np.int32)
val2 = np.ndarray(shape=(2, 0, 9), dtype=np.int32)
self._AssertDynamicStitchResultIs([idx1, idx2], [val1, val2],
                                  expected=np.ndarray(
                                      shape=(0, 9), dtype=np.int32))
