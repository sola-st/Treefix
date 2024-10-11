# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#47128
df = DataFrame({"a": ["a", "b"]})
df["b"] = df.index
df.loc[[False, True], "b"] = 100
result = df.loc[[1], :]
expected = DataFrame({"a": ["b"], "b": [100]}, index=[1])
tm.assert_frame_equal(result, expected)
