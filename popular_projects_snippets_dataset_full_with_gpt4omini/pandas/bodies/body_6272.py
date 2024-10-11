# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data[:5]
with pytest.raises(ValueError):
    arr[:1] = arr[:2]
