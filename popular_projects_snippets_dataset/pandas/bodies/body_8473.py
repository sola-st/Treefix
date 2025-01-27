# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH#2658
start = "2013-01-07"
idx = date_range(start=start, freq="1d", periods=10, tz="US/Eastern")
df = DataFrame(np.arange(10), index=idx)
df["2013-01-14 23:44:34.437768-05:00":]  # no exception here
