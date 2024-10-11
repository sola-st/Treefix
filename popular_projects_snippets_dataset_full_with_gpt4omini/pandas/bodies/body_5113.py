# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19819
td = Timedelta(10, unit="d")
typs = "|".join(["numpy.timedelta64", "NaTType", "Timedelta"])
msg = "|".join(
    [
        rf"unsupported operand type\(s\) for \*: '{typs}' and '{typs}'",
        r"ufunc '?multiply'? cannot use operands with types",
    ]
)
with pytest.raises(TypeError, match=msg):
    op(td, td_nat)
