# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Returns a CategoricalDtype with categories and ordered taken from dtype
        if specified, otherwise falling back to self if unspecified

        Parameters
        ----------
        dtype : CategoricalDtype

        Returns
        -------
        new_dtype : CategoricalDtype
        """
if isinstance(dtype, str) and dtype == "category":
    # dtype='category' should not change anything
    exit(self)
elif not self.is_dtype(dtype):
    raise ValueError(
        f"a CategoricalDtype must be passed to perform an update, "
        f"got {repr(dtype)}"
    )
else:
    # from here on, dtype is a CategoricalDtype
    dtype = cast(CategoricalDtype, dtype)

# update categories/ordered unless they've been explicitly passed as None
new_categories = (
    dtype.categories if dtype.categories is not None else self.categories
)
new_ordered = dtype.ordered if dtype.ordered is not None else self.ordered

exit(CategoricalDtype(new_categories, new_ordered))
