# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Make a Categorical type from codes and categories or dtype.

        This constructor is useful if you already have codes and
        categories/dtype and so do not need the (computation intensive)
        factorization step, which is usually done on the constructor.

        If your data does not follow this convention, please use the normal
        constructor.

        Parameters
        ----------
        codes : array-like of int
            An integer array, where each integer points to a category in
            categories or dtype.categories, or else is -1 for NaN.
        categories : index-like, optional
            The categories for the categorical. Items need to be unique.
            If the categories are not given here, then they must be provided
            in `dtype`.
        ordered : bool, optional
            Whether or not this categorical is treated as an ordered
            categorical. If not given here or in `dtype`, the resulting
            categorical will be unordered.
        dtype : CategoricalDtype or "category", optional
            If :class:`CategoricalDtype`, cannot be used together with
            `categories` or `ordered`.

        Returns
        -------
        Categorical

        Examples
        --------
        >>> dtype = pd.CategoricalDtype(['a', 'b'], ordered=True)
        >>> pd.Categorical.from_codes(codes=[0, 1, 0, 1], dtype=dtype)
        ['a', 'b', 'a', 'b']
        Categories (2, object): ['a' < 'b']
        """
dtype = CategoricalDtype._from_values_or_dtype(
    categories=categories, ordered=ordered, dtype=dtype
)
if dtype.categories is None:
    msg = (
        "The categories must be provided in 'categories' or "
        "'dtype'. Both were None."
    )
    raise ValueError(msg)

if is_extension_array_dtype(codes) and is_integer_dtype(codes):
    # Avoid the implicit conversion of Int to object
    if isna(codes).any():
        raise ValueError("codes cannot contain NA values")
    codes = codes.to_numpy(dtype=np.int64)
else:
    codes = np.asarray(codes)
if len(codes) and not is_integer_dtype(codes):
    raise ValueError("codes need to be array-like integers")

if len(codes) and (codes.max() >= len(dtype.categories) or codes.min() < -1):
    raise ValueError("codes need to be between -1 and len(categories)-1")

exit(cls(codes, dtype=dtype, fastpath=True))
