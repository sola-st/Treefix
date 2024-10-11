# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
ser = pd.Series(data)
with pytest.raises(TypeError, match="cannot perform|unsupported operand"):
    ser + data
