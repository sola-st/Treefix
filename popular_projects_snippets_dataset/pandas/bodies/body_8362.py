# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
# bug I fixed 12/20/2011
dates = pd.date_range("2011-01-01 04:00:00", periods=10, name="something")

formatted = dates.format(name=True)
assert formatted[0] == "something"
