# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = datetime_frame
msg = "Invalid value 'foo' for option 'date_unit'"
with pytest.raises(ValueError, match=msg):
    df.to_json(date_format="iso", date_unit="foo")
