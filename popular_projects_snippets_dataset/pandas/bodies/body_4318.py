# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

if op == "div":
    exit()

df = DataFrame({"a": [1.0, 2.0, 3.0], "b": [1, 2, 3]})

operand = 2
if op in ("and", "or", "xor"):
    # cannot use floats for boolean ops
    df["a"] = [True, False, True]

df_copy = df.copy()
iop = f"__i{op}__"
op = f"__{op}__"

# no id change and value is correct
getattr(df, iop)(operand)
expected = getattr(df_copy, op)(operand)
tm.assert_frame_equal(df, expected)
expected = id(df)
assert id(df) == expected
