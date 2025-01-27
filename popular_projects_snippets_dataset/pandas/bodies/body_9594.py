# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_arithmetic.py

op = all_arithmetic_operators
s = pd.Series(data)
ops = getattr(s, op)

# invalid scalars
msg = "|".join(
    [
        r"can only perform ops with numeric values",
        r"FloatingArray cannot perform the operation mod",
        "unsupported operand type",
        "not all arguments converted during string formatting",
        "can't multiply sequence by non-int of type 'float'",
        "ufunc 'subtract' cannot use operands with types dtype",
        r"can only concatenate str \(not \"float\"\) to str",
        "ufunc '.*' not supported for the input types, and the inputs could not",
        "ufunc '.*' did not contain a loop with signature matching types",
        "Concatenation operation is not implemented for NumPy arrays",
    ]
)
with pytest.raises(TypeError, match=msg):
    ops("foo")
with pytest.raises(TypeError, match=msg):
    ops(pd.Timestamp("20180101"))

# invalid array-likes
with pytest.raises(TypeError, match=msg):
    ops(pd.Series("foo", index=s.index))

msg = "|".join(
    [
        "can only perform ops with numeric values",
        "cannot perform .* with this index type: DatetimeArray",
        "Addition/subtraction of integers and integer-arrays "
        "with DatetimeArray is no longer supported. *",
        "unsupported operand type",
        "not all arguments converted during string formatting",
        "can't multiply sequence by non-int of type 'float'",
        "ufunc 'subtract' cannot use operands with types dtype",
        (
            "ufunc 'add' cannot use operands with types "
            rf"dtype\('{tm.ENDIAN}M8\[ns\]'\)"
        ),
        r"ufunc 'add' cannot use operands with types dtype\('float\d{2}'\)",
        "cannot subtract DatetimeArray from ndarray",
    ]
)
with pytest.raises(TypeError, match=msg):
    ops(pd.Series(pd.date_range("20180101", periods=len(s))))
