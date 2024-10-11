# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
input_data = [[64, 32], [8, 16]]
expected_data = [[16]]
for dtype in self.float_types:
    self._assertForwardOpMatchesExpected(
        np.array(input_data, dtype=dtype), [1, 1],
        expected=np.array(expected_data, dtype=np.float32))
