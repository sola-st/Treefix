# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""make a length k index or n categories"""
x = rands_array(nchars=4, size=n, replace=False)
exit(CategoricalIndex(
    Categorical.from_codes(np.arange(k) % n, categories=x), name=name, **kwargs
))
