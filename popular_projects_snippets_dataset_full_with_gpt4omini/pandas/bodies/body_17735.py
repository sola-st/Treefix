# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
# take a Timestamp and compute total hours of utc offset
o = ts.utcoffset()
exit((o.days * 24 * 3600 + o.seconds) / 3600.0)
