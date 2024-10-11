# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
input_data = [[64, 32], [32, 64], [50, 100]]
expected_data = [[64.0, 48.0, 32.0, 32.0], [48.0, 48.0, 48.0, 48.0],
                 [32.0, 48.0, 64.0, 64.0], [41.0, 61.5, 82.0, 82.0],
                 [50.0, 75.0, 100.0, 100.0], [50.0, 75.0, 100.0, 100.0]]
for dtype in self.float_types:
    self._assertForwardOpMatchesExpected(
        np.array(input_data, dtype=dtype), [6, 4],
        expected=np.array(expected_data, dtype=np.float32),
        align_corners=False)
