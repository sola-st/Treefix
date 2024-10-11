# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# Disallowed since 2.0 (GH 37819)
ser = Series(np.arange(10), date_range("2014-01-01", periods=10))

nonmonotonic = ser[[3, 5, 4]]
timestamp = Timestamp("2014-01-10")
with pytest.raises(
    KeyError, match="Value based partial slicing on non-monotonic"
):
    nonmonotonic["2014-01-10":]

with pytest.raises(KeyError, match=r"Timestamp\('2014-01-10 00:00:00'\)"):
    nonmonotonic[timestamp:]

with pytest.raises(
    KeyError, match="Value based partial slicing on non-monotonic"
):
    nonmonotonic.loc["2014-01-10":]

with pytest.raises(KeyError, match=r"Timestamp\('2014-01-10 00:00:00'\)"):
    nonmonotonic.loc[timestamp:]
