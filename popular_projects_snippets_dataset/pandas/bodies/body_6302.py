# Extracted from ./data/repos/pandas/pandas/tests/extension/base/accumulate.py
op_name = all_numeric_accumulations
ser = pd.Series(data)

with pytest.raises(NotImplementedError):
    getattr(ser, op_name)(skipna=skipna)
