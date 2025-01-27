# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
one = np.array(1., dtype=float_type)
two = np.array(2., dtype=float_type)
zero = np.array(0., dtype=float_type)
nan = np.array(np.nan, dtype=float_type)
np.testing.assert_equal(
    np.nextafter(one, two) - one, FLOAT_EPSILON[float_type])
np.testing.assert_equal(
    np.nextafter(one, zero) - one, -FLOAT_EPSILON[float_type] / 2)
np.testing.assert_equal(np.isnan(np.nextafter(nan, one)), True)
np.testing.assert_equal(np.isnan(np.nextafter(one, nan)), True)
np.testing.assert_equal(np.nextafter(one, one), one)
smallest_denormal = FLOAT_SMALLEST_SUBNORMAL[float_type]
np.testing.assert_equal(np.nextafter(zero, one), smallest_denormal)
np.testing.assert_equal(np.nextafter(zero, -one), -smallest_denormal)
for a, b in itertools.permutations([0., nan], 2):
    np.testing.assert_equal(
        np.nextafter(
            np.array(a, dtype=np.float32), np.array(b, dtype=np.float32)),
        np.nextafter(
            np.array(a, dtype=float_type), np.array(b, dtype=float_type)))
