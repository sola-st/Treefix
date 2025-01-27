# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH#46560
df = DataFrame({"a": [1, 2, 3], "b": 2, "c": 3})
df["c"] = df["c"].astype(object)
arg = (df,) if use_arg else ()
expanding = df.expanding()
op = getattr(expanding, kernel)
result = op(*arg, numeric_only=numeric_only)

# Compare result to op using float dtypes, dropping c when numeric_only is True
columns = ["a", "b"] if numeric_only else ["a", "b", "c"]
df2 = df[columns].astype(float)
arg2 = (df2,) if use_arg else ()
expanding2 = df2.expanding()
op2 = getattr(expanding2, kernel)
expected = op2(*arg2, numeric_only=numeric_only)

tm.assert_frame_equal(result, expected)
