# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#8554, GH#22163 DataFrame op should _not_ return dt64 dtype
idx = date_range("2013-01-01", periods=3)._with_freq(None)
idx = tm.box_expected(idx, box_with_array)

expected = TimedeltaIndex(["0 Days", "1 Day", "2 Days"])
expected = tm.box_expected(expected, box_with_array)

result = idx - ts
tm.assert_equal(result, expected)

result = ts - idx
tm.assert_equal(result, -expected)
tm.assert_equal(result, -expected)
