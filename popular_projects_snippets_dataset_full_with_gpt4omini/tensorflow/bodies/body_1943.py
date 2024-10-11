# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
input_data = [[127, 127, 64, 64], [127, 127, 64, 64], [64, 64, 127, 127],
              [64, 64, 127, 127], [50, 50, 100, 100], [50, 50, 100, 100]]
expected_data = [[127, 64], [64, 127], [50, 100]]
for dtype in self.float_types:
    self._assertForwardOpMatchesExpected(
        np.array(input_data, dtype=dtype), [3, 2],
        expected=np.array(expected_data, dtype=dtype),
        align_corners=False)
