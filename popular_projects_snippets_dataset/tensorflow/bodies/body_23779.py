# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for v in FLOAT_VALUES[float_type]:
    np.testing.assert_equal(
        float(float_type(-float(float_type(v)))), float(-float_type(v)))
