# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH25433 GH25435
df = DataFrame([[1, 2], [3, 4]], index=[1.0, 2.0], columns=["1.", "2."])
dfjson = df.to_json(orient="table")
msg = "cannot pass both convert_axes and orient='table'"
with pytest.raises(ValueError, match=msg):
    read_json(dfjson, orient="table", convert_axes=True)
