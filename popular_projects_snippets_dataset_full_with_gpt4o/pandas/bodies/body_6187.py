# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
ub = len(data)

with pytest.raises(IndexError):
    data.insert(ub + 1, data[0])

with pytest.raises(IndexError):
    data.insert(-ub - 1, data[0])

with pytest.raises(TypeError):
    # we expect TypeError here instead of IndexError to match np.insert
    data.insert(1.5, data[0])
