# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
empty_series = Series([], index=[], dtype=np.float64)
data = empty_series.to_json(orient=orient)
result = read_json(data, typ="series", orient=orient)

expected = empty_series
if orient in ("values", "records"):
    expected = expected.reset_index(drop=True)
else:
    expected.index = expected.index.astype(float)

tm.assert_series_equal(result, expected)
