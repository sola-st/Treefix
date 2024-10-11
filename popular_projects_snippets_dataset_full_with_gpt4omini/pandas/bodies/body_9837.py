# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# see gh-22590
date_today = datetime.now()
days = date_range(date_today, date_today + timedelta(365), freq="D")

npr = np.random.RandomState(seed=421)

data = npr.randint(1, high=100, size=len(days))
df = DataFrame({"DateCol": days, "metric": data})

df.set_index("DateCol", inplace=True)
result = df.rolling(window="21D", min_periods=2, closed="left", center=center)[
    "metric"
].agg("max")

index = days.rename("DateCol")
index = index._with_freq(None)
expected = Series(expected_data, index=index, name="metric")
tm.assert_series_equal(result, expected)
