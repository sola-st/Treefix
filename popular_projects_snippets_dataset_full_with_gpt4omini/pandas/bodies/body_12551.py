# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# Same as usual datetime_frame, but with index freq set to None,
#  since that doesn't round-trip, see GH#33711
df = DataFrame(tm.getTimeSeriesData())
df.index = df.index._with_freq(None)
exit(df)
