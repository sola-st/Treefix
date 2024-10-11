# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#12533
ser = Series(4, index=list("ABCD"))
result = ser[lambda x: "A"]
assert result == ser.loc["A"]

result = ser[lambda x: ["A", "B"]]
expected = ser.loc[["A", "B"]]
tm.assert_series_equal(result, expected)

result = ser[lambda x: [True, False, True, True]]
expected = ser.iloc[[0, 2, 3]]
tm.assert_series_equal(result, expected)
