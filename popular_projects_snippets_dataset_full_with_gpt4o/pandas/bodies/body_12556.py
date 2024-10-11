# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame([["a", "b"], ["c", "d"]], index=[1, 2], columns=["x", "x"])

msg = f"DataFrame columns must be unique for orient='{orient}'"
with pytest.raises(ValueError, match=msg):
    df.to_json(orient=orient)
