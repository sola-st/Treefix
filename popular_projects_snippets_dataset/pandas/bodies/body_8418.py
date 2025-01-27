# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#1673 smoke test
dr = date_range("2012-01-01", "2012-01-10", freq="D", tz="Hongkong")

# it works!
dr.hour
