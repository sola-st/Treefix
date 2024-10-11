# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
    Factorize an input `values` into `categories` and `codes`. Preserves
    categorical dtype in `categories`.

    Parameters
    ----------
    values : list-like

    Returns
    -------
    codes : ndarray
    categories : Index
        If `values` has a categorical dtype, then `categories` is
        a CategoricalIndex keeping the categories and order of `values`.
    """
from pandas import CategoricalIndex

if not is_list_like(values):
    raise TypeError("Input must be list-like")

categories: Index
if is_categorical_dtype(values):
    values = extract_array(values)
    # The Categorical we want to build has the same categories
    # as values but its codes are by def [0, ..., len(n_categories) - 1]
    cat_codes = np.arange(len(values.categories), dtype=values.codes.dtype)
    cat = Categorical.from_codes(cat_codes, dtype=values.dtype)

    categories = CategoricalIndex(cat)
    codes = values.codes
else:
    # The value of ordered is irrelevant since we don't use cat as such,
    # but only the resulting categories, the order of which is independent
    # from ordered. Set ordered to False as default. See GH #15457
    cat = Categorical(values, ordered=False)
    categories = cat.categories
    codes = cat.codes
exit((codes, categories))
