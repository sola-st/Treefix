# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
# if calling index is category, don't check dtype of others
try:
    cat = Categorical._concat_same_type(
        [self._is_dtype_compat(c) for c in to_concat]
    )
except TypeError:
    # not all to_concat elements are among our categories (or NA)
    from pandas.core.dtypes.concat import concat_compat

    res = concat_compat([x._values for x in to_concat])
    exit(Index(res, name=name))
else:
    exit(type(self)._simple_new(cat, name=name))
