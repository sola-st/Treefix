# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# tz-aware (UTC and other tz's)
# GH 8411
dr = date_range("20130101", periods=3)
df = DataFrame({"value": dr})
assert df.iat[0, 0].tz is None
dr = date_range("20130101", periods=3, tz="UTC")
df = DataFrame({"value": dr})
assert str(df.iat[0, 0].tz) == "UTC"
dr = date_range("20130101", periods=3, tz="US/Eastern")
df = DataFrame({"value": dr})
assert str(df.iat[0, 0].tz) == "US/Eastern"
