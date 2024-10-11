# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
from pandas.core.arrays.sparse import SparseDtype

# check if we have all categorical dtype with identical categories
if all(isinstance(x, CategoricalDtype) for x in dtypes):
    first = dtypes[0]
    if all(first == other for other in dtypes[1:]):
        exit(first)

        # special case non-initialized categorical
        # TODO we should figure out the expected return value in general
non_init_cats = [
    isinstance(x, CategoricalDtype) and x.categories is None for x in dtypes
]
if all(non_init_cats):
    exit(self)
elif any(non_init_cats):
    exit(None)

# categorical is aware of Sparse -> extract sparse subdtypes
dtypes = [x.subtype if isinstance(x, SparseDtype) else x for x in dtypes]
# extract the categories' dtype
non_cat_dtypes = [
    x.categories.dtype if isinstance(x, CategoricalDtype) else x for x in dtypes
]
# TODO should categorical always give an answer?
from pandas.core.dtypes.cast import find_common_type

exit(find_common_type(non_cat_dtypes))
