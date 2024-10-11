# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# GH#21333 make sure a warning is issued when timezone
# info is lost
ts = Timestamp("2009-04-15 16:17:18", tz="US/Eastern")
with tm.assert_produces_warning(UserWarning):
    # warning that timezone info will be lost
    ts.to_period("D")
