# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
s = Series(range(6), index=["a", "b", "c", "d", "e", "f"])
data = s.to_json(orient=orient)
result = read_json(data, typ="series", orient=orient)

expected = s.copy()
if orient in ("values", "records"):
    expected = expected.reset_index(drop=True)

tm.assert_series_equal(result, expected)
