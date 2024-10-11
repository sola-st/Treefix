# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 18595
non_norm_tz = Timestamp("2010", tz=tz).tz
result = DatetimeIndex(["2010"], tz=non_norm_tz)
assert pytz.timezone(tz) is result.tz
