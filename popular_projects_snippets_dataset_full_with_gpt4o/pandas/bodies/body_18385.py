# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#39750 make sure we infer the result as td64
tdi = TimedeltaIndex([NaT, NaT])

left = tm.box_expected(tdi, box_with_array)
right = np.array([2, 2.0], dtype=object)

expected = pd.Index([np.timedelta64("NaT", "ns")] * 2, dtype=object)
if box_with_array is not pd.Index:
    expected = tm.box_expected(expected, box_with_array).astype(object)

result = left / right
tm.assert_equal(result, expected)

result = left // right
tm.assert_equal(result, expected)
