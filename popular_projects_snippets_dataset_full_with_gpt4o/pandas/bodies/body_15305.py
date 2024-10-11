# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
# GH14826, indexing with a seconds resolution string / datetime object
df = DataFrame(
    np.random.rand(5, 5),
    columns=["open", "high", "low", "close", "volume"],
    index=date_range("2012-01-02 18:01:00", periods=5, tz="US/Central", freq="s"),
)

# this is a single date, so will raise
with pytest.raises(KeyError, match=r"^'2012-01-02 18:01:02'$"):
    df["2012-01-02 18:01:02"]

msg = r"Timestamp\('2012-01-02 18:01:02-0600', tz='US/Central'\)"
with pytest.raises(KeyError, match=msg):
    df[df.index[2]]
