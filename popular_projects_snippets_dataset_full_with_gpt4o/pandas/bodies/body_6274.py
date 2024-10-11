# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data[:5].copy()
with pytest.raises(ValueError):
    arr[0] = arr[[0, 1]]
