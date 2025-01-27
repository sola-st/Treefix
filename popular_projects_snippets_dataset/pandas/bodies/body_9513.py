# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
# invalid ops

op = all_arithmetic_operators
s = pd.Series(data)
ops = getattr(s, op)

# invalid scalars
msg = (
    "did not contain a loop with signature matching types|"
    "BooleanArray cannot perform the operation|"
    "not supported for the input types, and the inputs could not be safely coerced "
    "to any supported types according to the casting rule ''safe''"
)
with pytest.raises(TypeError, match=msg):
    ops("foo")
msg = "|".join(
    [
        r"unsupported operand type\(s\) for",
        "Concatenation operation is not implemented for NumPy arrays",
    ]
)
with pytest.raises(TypeError, match=msg):
    ops(pd.Timestamp("20180101"))

# invalid array-likes
if op not in ("__mul__", "__rmul__"):
    # TODO(extension) numpy's mul with object array sees booleans as numbers
    msg = "|".join(
        [
            r"unsupported operand type\(s\) for",
            "can only concatenate str",
            "not all arguments converted during string formatting",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        ops(pd.Series("foo", index=s.index))
