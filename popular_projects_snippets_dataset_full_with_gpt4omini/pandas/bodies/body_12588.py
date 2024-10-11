# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
s = Series([1, 2, 3])
msg = "Invalid value 'garbage' for option 'orient'"
with pytest.raises(ValueError, match=msg):
    s.to_json(orient="garbage")
