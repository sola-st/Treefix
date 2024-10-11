# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH21345
df = DataFrame({"a": [1, 2], "b": [3.0, 4.0], "c": ["5", "6"]})
dfjson = df.to_json(orient="table")
msg = "cannot pass both dtype and orient='table'"
with pytest.raises(ValueError, match=msg):
    read_json(dfjson, orient="table", dtype=dtype)
