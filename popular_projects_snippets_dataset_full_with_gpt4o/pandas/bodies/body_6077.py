# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
result = data[0]
assert isinstance(result, data.dtype.type)

result = pd.Series(data)[0]
assert isinstance(result, data.dtype.type)
