# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
item = invalid_scalar

with pytest.raises((TypeError, ValueError)):
    data.insert(0, item)

with pytest.raises((TypeError, ValueError)):
    data.insert(4, item)

with pytest.raises((TypeError, ValueError)):
    data.insert(len(data) - 1, item)
