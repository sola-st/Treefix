# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#48190
df = DataFrame({"a": [1, 2]}, dtype=any_numeric_ea_dtype)
result = df.reindex(columns=list("ab"), index=[0, 1, 2], fill_value=10)
expected = DataFrame(
    {"a": Series([1, 2, 10], dtype=any_numeric_ea_dtype), "b": 10}
)
tm.assert_frame_equal(result, expected)
