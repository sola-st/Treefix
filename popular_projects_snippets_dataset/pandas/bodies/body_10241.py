# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# it works!
df = DataFrame(
    [(3, np.datetime64("2012-07-03")), (3, np.datetime64("2012-07-04"))],
    columns=["a", "date"],
)
result = df.groupby("a").first()
assert result["date"][3] == Timestamp("2012-07-03")
