# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
s = tm.makeFloatSeries()
tm.assert_series_equal(np.squeeze(s), s)

df = tm.makeTimeDataFrame().reindex(columns=["A"])
tm.assert_series_equal(np.squeeze(df), df["A"])
