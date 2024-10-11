# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
ser = pd.Series(data)
with pytest.raises(TypeError, match="unsupported"):
    ser + data
