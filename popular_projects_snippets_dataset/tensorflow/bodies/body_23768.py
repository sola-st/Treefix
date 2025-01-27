# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for v in INT_VALUES[float_type]:
    self.assertEqual(v, int(float_type(v)))
    self.assertEqual(-v, int(float_type(-v)))
