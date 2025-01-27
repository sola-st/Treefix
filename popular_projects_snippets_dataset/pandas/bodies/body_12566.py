# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
with pytest.raises(ValueError, match=msg):
    read_json(StringIO(data), orient=orient)
