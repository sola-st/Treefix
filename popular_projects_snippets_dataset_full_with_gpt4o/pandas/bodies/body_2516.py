# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#37366
class mystring(str):
    pass

data = ["2020-10-22 01:21:00+00:00"]
index = DatetimeIndex(data)
df = DataFrame({"a": [1]}, index=index)
df["b"] = 2
df[mystring("c")] = 3
expected = DataFrame({"a": [1], "b": [2], mystring("c"): [3]}, index=index)
tm.assert_equal(df, expected)
