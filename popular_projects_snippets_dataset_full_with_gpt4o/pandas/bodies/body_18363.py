# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#20088, GH#22163 ensure DataFrame returns correct dtype
box = box_with_array
xbox = np.ndarray if box is pd.array else box

rng = timedelta_range("1 days", "10 days", name="foo")
expected = NumericIndex((np.arange(10) + 1) * 12, dtype=np.float64, name="foo")

rng = tm.box_expected(rng, box)
expected = tm.box_expected(expected, xbox)

result = rng / two_hours
tm.assert_equal(result, expected)

result = two_hours / rng
expected = 1 / expected
tm.assert_equal(result, expected)
