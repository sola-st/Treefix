# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH6529
# coerce datetime64 non-ns properly
dates = date_range("01-Jan-2015", "01-Dec-2015", freq="M")
values2 = dates.view(np.ndarray).astype("datetime64[ns]")
expected = Series(values2, index=dates)

for unit in ["s", "D", "ms", "us", "ns"]:
    dtype = np.dtype(f"M8[{unit}]")
    values1 = dates.view(np.ndarray).astype(dtype)
    result = Series(values1, dates)
    if unit == "D":
        # for unit="D" we cast to nearest-supported reso, i.e. "s"
        dtype = np.dtype("M8[s]")
    assert result.dtype == dtype
    tm.assert_series_equal(result, expected.astype(dtype))

# GH 13876
# coerce to non-ns to object properly
expected = Series(values2, index=dates, dtype=object)
for dtype in ["s", "D", "ms", "us", "ns"]:
    values1 = dates.view(np.ndarray).astype(f"M8[{dtype}]")
    result = Series(values1, index=dates, dtype=object)
    tm.assert_series_equal(result, expected)

# leave datetime.date alone
dates2 = np.array([d.date() for d in dates.to_pydatetime()], dtype=object)
series1 = Series(dates2, dates)
tm.assert_numpy_array_equal(series1.values, dates2)
assert series1.dtype == object
