# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 20671, getting value not in dict raising `KeyError`
ser = Series([(1, 2, 3), [1, 2, 3], {1, 2, 3}, {1: "a", 2: "b", 3: "c"}])

result = ser.str.get(idx)
expected = Series(exp)
tm.assert_series_equal(result, expected)
