# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#42530

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
result = df.pop("b")
result[[True, False, False]] = 9
expected = Series(data=[9, 5, 6], name="b")
tm.assert_series_equal(result, expected)

df.loc[[True, False, False], "a"] = 10
expected = DataFrame({"a": [10, 2, 3]})
tm.assert_frame_equal(df, expected)
