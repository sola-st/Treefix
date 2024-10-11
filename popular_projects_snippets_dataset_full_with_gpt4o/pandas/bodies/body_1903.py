# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 19375
index = date_range("2017-03-12", "2017-03-12 1:45:00", freq="15T")
s = Series(np.zeros(len(index)), index=index)
expected = s.tz_localize("US/Pacific")
expected.index = pd.DatetimeIndex(expected.index, freq="900S")
result = expected.resample("900S").mean()
tm.assert_series_equal(result, expected)

# GH 23742
index = date_range(start="2017-10-10", end="2017-10-20", freq="1H")
index = index.tz_localize("UTC").tz_convert("America/Sao_Paulo")
df = DataFrame(data=list(range(len(index))), index=index)
result = df.groupby(pd.Grouper(freq="1D")).count()
expected = date_range(
    start="2017-10-09",
    end="2017-10-20",
    freq="D",
    tz="America/Sao_Paulo",
    nonexistent="shift_forward",
    inclusive="left",
)
tm.assert_index_equal(result.index, expected)
