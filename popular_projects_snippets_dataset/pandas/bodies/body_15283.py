# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH#48614
df = DataFrame({"a": [1]})
ser = Series({"label": df})
ser.loc["new_label"] = df
expected = Series({"label": df, "new_label": df})
tm.assert_series_equal(ser, expected)
