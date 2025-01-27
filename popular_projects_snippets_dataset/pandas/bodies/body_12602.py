# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
ts = Series(Timestamp(date), index=datetime_series.index)
ts.iloc[1] = pd.NaT
ts.iloc[5] = pd.NaT
if date_unit:
    json = ts.to_json(date_format="iso", date_unit=date_unit)
else:
    json = ts.to_json(date_format="iso")
result = read_json(json, typ="series")
expected = ts.copy()
tm.assert_series_equal(result, expected)
