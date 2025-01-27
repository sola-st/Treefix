# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
arr = data[:3]

with pytest.raises(IndexError, match="out of bounds|out-of-bounds"):
    arr.take(np.asarray([0, 3]), allow_fill=allow_fill)
