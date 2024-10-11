# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 15306
dates = date_range("1/1/2011", periods=10, freq="D")

stocks = DataFrame({"price": np.arange(10.0)}, index=dates)
stocks["week_id"] = dates.isocalendar().week

result = stocks.groupby(stocks["week_id"])["price"].transform(func)

expected = Series(data=pd.to_datetime(values), index=dates, name="price")

tm.assert_series_equal(result, expected)
