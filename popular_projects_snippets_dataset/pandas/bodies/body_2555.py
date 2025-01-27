# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH 28928
result = DataFrame({"a": [3, 4], "b": [5, 6]}).astype(
    {"a": "int64", "b": "Int64"}
)
mask = Series(False, index=result.index)
result.loc[mask, "a"] = result["a"]
result.loc[mask, "b"] = result["b"]
expected = DataFrame({"a": [3, 4], "b": [5, 6]}).astype(
    {"a": "int64", "b": "Int64"}
)
tm.assert_frame_equal(result, expected)
