# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
box = box_with_array
obj = tm.box_expected(interval_array, box)
result = op(obj, nulls_fixture)

if nulls_fixture is pd.NA:
    # GH#31882
    exp = np.ones(interval_array.shape, dtype=bool)
    expected = BooleanArray(exp, exp)
else:
    expected = self.elementwise_comparison(op, interval_array, nulls_fixture)

if not (box is Index and nulls_fixture is pd.NA):
    # don't cast expected from BooleanArray to ndarray[object]
    xbox = get_upcast_box(obj, nulls_fixture, True)
    expected = tm.box_expected(expected, xbox)

tm.assert_equal(result, expected)

rev = op(nulls_fixture, obj)
tm.assert_equal(rev, expected)
