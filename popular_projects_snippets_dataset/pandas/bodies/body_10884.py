# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# test for #13393, where DataframeGroupBy.count() fails
# when counting a datetimelike column.

df = DataFrame({"x": ["a", "a", "b"], "y": datetimelike})
res = df.groupby("x").count()
expected = DataFrame({"y": [2, 1]}, index=["a", "b"])
expected.index.name = "x"
tm.assert_frame_equal(expected, res)
