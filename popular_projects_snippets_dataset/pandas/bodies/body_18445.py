# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
dti = DatetimeIndex(["2011-01-01", "2011-01-02"], freq=dti_freq)
dtarr = tm.box_expected(dti, box_with_array)
msg = "|".join(
    [
        "unsupported operand type",
        "cannot (add|subtract)",
        "cannot use operands with types",
        "ufunc '?(add|subtract)'? cannot use operands with types",
        "Concatenation operation is not implemented for NumPy arrays",
    ]
)
assert_invalid_addsub_type(dtarr, other, msg)
