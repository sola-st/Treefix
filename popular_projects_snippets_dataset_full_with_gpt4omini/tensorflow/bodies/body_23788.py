# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for v in FLOAT_VALUES[float_type]:
    for w in FLOAT_VALUES[float_type]:
        self.assertEqual(v > w, float_type(v) > float_type(w))
