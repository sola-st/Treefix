# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py

# tst ops and reversed ops in evaluation
# GH7198

df = DataFrame(1, index=range(n), columns=list("abcd"))
df.iloc[0] = 2
m = df.mean()

base = DataFrame(  # noqa:F841
    np.tile(m.values, n).reshape(n, -1), columns=list("abcd")
)

expected = eval(f"base {op_str} df")

# ops as strings
result = eval(f"m {op_str} df")
tm.assert_frame_equal(result, expected)

# these are commutative
if op in ["+", "*"]:
    result = getattr(df, op)(m)
    tm.assert_frame_equal(result, expected)

# these are not
elif op in ["-", "/"]:
    result = getattr(df, rop)(m)
    tm.assert_frame_equal(result, expected)
