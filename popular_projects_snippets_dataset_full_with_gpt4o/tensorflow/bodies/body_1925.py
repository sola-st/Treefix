# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
# TODO(b/72099414): enable the test for TPU when the issue is fixed.
if (self.device not in ["XLA_GPU", "XLA_CPU"]):
    exit()
# Ensure that resize with convolution works on XLA/GPU for integer types
self._assertForwardOpMatchesExpected(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8), [12, 12],
    expected=np.array([[1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3],
                       [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3],
                       [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6],
                       [7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9],
                       [7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9],
                       [7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9]],
                      dtype=np.uint8))
