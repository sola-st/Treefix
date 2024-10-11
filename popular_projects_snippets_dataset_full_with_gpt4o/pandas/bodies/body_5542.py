# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
kwarg = {arg: 1}
msg = "Cannot pass a date attribute keyword argument"
with pytest.raises(ValueError, match=msg):
    Timestamp("2010-10-10 12:59:59.999999999", **kwarg)
