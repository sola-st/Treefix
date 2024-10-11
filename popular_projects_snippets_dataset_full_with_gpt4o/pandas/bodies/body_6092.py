# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
result = data.take([0, -1])
assert result.dtype == data.dtype
assert result[0] == data[0]
assert result[1] == data[-1]

result = data.take([0, -1], allow_fill=True, fill_value=na_value)
assert result[0] == data[0]
assert na_cmp(result[1], na_value)

with pytest.raises(IndexError, match="out of bounds"):
    data.take([len(data) + 1])
