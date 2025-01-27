# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#14621, GH#7825
# assert conversion to naive is the same as replacing tzinfo with None
ts = Timestamp("2013-11-03 01:59:59.999999-0400", tz="US/Eastern")
assert ts.tz_localize(None) == ts.replace(tzinfo=None)
