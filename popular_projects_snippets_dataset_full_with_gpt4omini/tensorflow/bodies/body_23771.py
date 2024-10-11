# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for value in FLOAT_VALUES[float_type]:
    self.assertEqual("%.6g" % float(float_type(value)),
                     str(float_type(value)))
