# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#20049 subtracting PeriodIndex should raise TypeError
dti = DatetimeIndex(["2011-01-01", "2011-01-02"], freq=dti_freq)
pi = dti.to_period(pi_freq)

dtarr = tm.box_expected(dti, box_with_array)
parr = tm.box_expected(pi, box_with_array2)
msg = "|".join(
    [
        "cannot (add|subtract)",
        "unsupported operand",
        "descriptor.*requires",
        "ufunc.*cannot use operands",
    ]
)
assert_invalid_addsub_type(dtarr, parr, msg)
