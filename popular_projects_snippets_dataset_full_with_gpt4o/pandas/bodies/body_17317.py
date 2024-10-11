# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# squeezing
df = tm.makeTimeDataFrame().reindex(columns=["A"])
tm.assert_series_equal(df.squeeze(), df["A"])
