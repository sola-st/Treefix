# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
# Sweep a variety of binades to see that spacing gives the proper ULP.
with self.subTest(name="Subnormals"):
    for i in range(
        int(np.log2(FLOAT_SMALLEST_SUBNORMAL[float_type])),
        int(np.log2(FLOAT_SMALLEST_NORMAL[float_type]))):
        power_of_two = float_type(2.0**i)
        distance = FLOAT_SMALLEST_SUBNORMAL[float_type]
        np.testing.assert_equal(np.spacing(power_of_two), distance)
        np.testing.assert_equal(np.spacing(-power_of_two), -distance)
    # Normals have a distance which depends on their binade.
with self.subTest(name="Normals"):
    for i in range(
        int(np.log2(FLOAT_SMALLEST_NORMAL[float_type])),
        int(np.log2(FLOAT_MAX[float_type]))):
        power_of_two = float_type(2.0**i)
        distance = FLOAT_EPSILON[float_type] * power_of_two
        np.testing.assert_equal(np.spacing(power_of_two), distance)
        np.testing.assert_equal(np.spacing(-power_of_two), -distance)

    # Check that spacing agrees with arithmetic involving nextafter.
with self.subTest(name="NextAfter"):
    for x in FLOAT_VALUES[float_type]:
        x_float_type = float_type(x)
        spacing = np.spacing(x_float_type)
        toward = np.copysign(float_type(2.0 * np.abs(x) + 1), x_float_type)
        nextup = np.nextafter(x_float_type, toward)
        if np.isnan(spacing):
            self.assertTrue(np.isnan(nextup - x_float_type))
        else:
            np.testing.assert_equal(spacing, nextup - x_float_type)

    # Check that spacing for special values gives the correct answer.
with self.subTest(name="NonFinite"):
    nan = float_type(float("nan"))
    np.testing.assert_equal(np.spacing(nan), np.spacing(np.float32(nan)))
    if dtype_has_inf(float_type):
        inf = float_type(float("inf"))
        np.testing.assert_equal(np.spacing(inf), np.spacing(np.float32(inf)))
