# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#15470
ser = Series(["a", "b", "c"], index=pd.CategoricalIndex([2, 1, 0]))

# 0 is treated as a label
assert ser[0] == "c"

# the listlike analogue should also be treated as labels
res = ser[[0]]
expected = ser.iloc[-1:]
tm.assert_series_equal(res, expected)

res2 = ser[[0, 1, 2]]
tm.assert_series_equal(res2, ser.iloc[::-1])
