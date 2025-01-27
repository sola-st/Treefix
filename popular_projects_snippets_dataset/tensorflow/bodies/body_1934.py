# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
input_data = [[64, 32], [8, 16], [50, 100]]
expected_data = [[64.0, 64.0, 32.0], [64.0, 64.0, 32.0], [8.0, 8.0, 16.0],
                 [8.0, 8.0, 16.0], [50.0, 50.0, 100.0]]
for dtype in self.float_types:
    self._assertForwardOpMatchesExpected(
        np.array(input_data, dtype=dtype), [5, 3],
        expected=np.array(expected_data, dtype=np.float32),
        half_pixel_centers=False)
