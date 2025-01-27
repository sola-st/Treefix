# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for value in np.extract(
    np.isfinite(FLOAT_VALUES[float_type]), FLOAT_VALUES[float_type]):
    with self.subTest(value):
        self.assertEqual(hash(value), hash(float_type(value)), str(value))
