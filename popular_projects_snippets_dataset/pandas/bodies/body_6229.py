# Extracted from ./data/repos/pandas/pandas/tests/extension/base/printing.py
ser = pd.Series(data)
assert data.dtype.name in repr(ser)
