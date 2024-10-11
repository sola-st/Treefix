# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
data = object_series.to_json(orient=orient)
result = read_json(data, typ="series", orient=orient, dtype=dtype)

expected = object_series
if orient in ("values", "records"):
    expected = expected.reset_index(drop=True)
if orient != "split":
    expected.name = None

tm.assert_series_equal(result, expected)
