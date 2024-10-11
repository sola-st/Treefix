# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
ts = Series(Timestamp("20130101 20:43:42.123"), index=datetime_series.index)
msg = "Invalid value 'foo' for option 'date_unit'"
with pytest.raises(ValueError, match=msg):
    ts.to_json(date_format="iso", date_unit="foo")
