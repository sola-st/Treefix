# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
index = pd.DatetimeIndex(())
data = ()
series = Series(data, index, dtype=object)
grouper = Grouper(freq="D")
grouped = series.groupby(grouper)
assert next(iter(grouped), None) is None
