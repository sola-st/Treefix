# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
a = float_type(a)
b = float_type(b)
expected = op(np.float32(a), np.float32(b))
result = op(a, b)
if math.isnan(expected):
    if not math.isnan(result):
        raise AssertionError("%s expected to be nan." % repr(result))
else:
    np.testing.assert_equal(
        truncate(expected, float_type=float_type), float(result))
