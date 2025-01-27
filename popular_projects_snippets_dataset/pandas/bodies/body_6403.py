# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
op_name = all_numeric_reductions

if op_name in ["min", "max"]:
    exit(None)

ser = pd.Series(data)
with pytest.raises(TypeError):
    getattr(ser, op_name)(skipna=skipna)
