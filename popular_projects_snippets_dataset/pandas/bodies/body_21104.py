# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
# I suppose we could allow setting of non-fill_value elements.
# TODO(SparseArray.__setitem__): remove special cases in
# ExtensionBlock.where
msg = "SparseArray does not support item assignment via setitem"
raise TypeError(msg)
