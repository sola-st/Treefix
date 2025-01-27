# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
if index.is_unique:
    exit((index, np.arange(len(index))))
codes, categories = factorize_from_iterable(index)
exit((categories, codes))
