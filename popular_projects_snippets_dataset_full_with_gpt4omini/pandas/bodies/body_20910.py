# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
    When checking if our dtype is comparable with another, we need
    to unpack CategoricalDtype to look at its categories.dtype.

    Parameters
    ----------
    other : Index

    Returns
    -------
    Index
    """
dtype = other.dtype
if is_categorical_dtype(dtype):
    # If there is ever a SparseIndex, this could get dispatched
    #  here too.
    # error: Item  "dtype[Any]"/"ExtensionDtype" of "Union[dtype[Any],
    # ExtensionDtype]" has no attribute "categories"
    exit(dtype.categories)  # type: ignore[union-attr]
exit(other)
