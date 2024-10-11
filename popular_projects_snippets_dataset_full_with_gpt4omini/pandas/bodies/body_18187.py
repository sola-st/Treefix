# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
box = box_with_array

left = tm.box_expected(numeric_idx, box)
msg = "|".join(
    [
        "unsupported operand type",
        "Addition/subtraction of integers and integer-arrays",
        "Instead of adding/subtracting",
        "cannot use operands with types dtype",
        "Concatenation operation is not implemented for NumPy arrays",
        "Cannot (add|subtract) NaT (to|from) ndarray",
        # pd.array vs np.datetime64 case
        r"operand type\(s\) all returned NotImplemented from __array_ufunc__",
        "can only perform ops with numeric values",
        "cannot subtract DatetimeArray from ndarray",
        # pd.Timedelta(1) + Index([0, 1, 2])
        "Cannot add or subtract Timedelta from integers",
    ]
)
assert_invalid_addsub_type(left, other, msg)
