# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py

op = all_arithmetic_operators
s = pd.Series(data)
ops = getattr(s, op)

# invalid scalars
msg = "|".join(
    [
        r"can only perform ops with numeric values",
        r"IntegerArray cannot perform the operation mod",
        r"unsupported operand type",
        r"can only concatenate str \(not \"int\"\) to str",
        "not all arguments converted during string",
        "ufunc '.*' not supported for the input types, and the inputs could not",
        "ufunc '.*' did not contain a loop with signature matching types",
        "Addition/subtraction of integers and integer-arrays with Timestamp",
    ]
)
with pytest.raises(TypeError, match=msg):
    ops("foo")
with pytest.raises(TypeError, match=msg):
    ops(pd.Timestamp("20180101"))

# invalid array-likes
str_ser = pd.Series("foo", index=s.index)
# with pytest.raises(TypeError, match=msg):
if all_arithmetic_operators in [
    "__mul__",
    "__rmul__",
]:  # (data[~data.isna()] >= 0).all():
    res = ops(str_ser)
    expected = pd.Series(["foo" * x for x in data], index=s.index)
    tm.assert_series_equal(res, expected)
else:
    with pytest.raises(TypeError, match=msg):
        ops(str_ser)

msg = "|".join(
    [
        "can only perform ops with numeric values",
        "cannot perform .* with this index type: DatetimeArray",
        "Addition/subtraction of integers and integer-arrays "
        "with DatetimeArray is no longer supported. *",
        "unsupported operand type",
        r"can only concatenate str \(not \"int\"\) to str",
        "not all arguments converted during string",
        "cannot subtract DatetimeArray from ndarray",
    ]
)
with pytest.raises(TypeError, match=msg):
    ops(pd.Series(pd.date_range("20180101", periods=len(s))))
