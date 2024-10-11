# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
if not is_categorical_dtype(data.dtype):
    raise AttributeError("Can only use .cat accessor with a 'category' dtype")
