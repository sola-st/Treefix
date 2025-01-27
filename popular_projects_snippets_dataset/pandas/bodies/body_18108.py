# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py

idx = PeriodIndex(["2017", "2017", "2018"], freq="D")
idx = tm.box_expected(idx, box_with_array)
xbox = get_upcast_box(idx, other, True)

expected = np.array([True, True, False])
expected = tm.box_expected(expected, xbox)

result = idx == other

tm.assert_equal(result, expected)
