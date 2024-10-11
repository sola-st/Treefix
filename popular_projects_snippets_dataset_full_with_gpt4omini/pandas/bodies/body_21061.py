# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
    Convert a set of codes for to a new set of categories

    Parameters
    ----------
    codes : np.ndarray
    old_categories, new_categories : Index
    copy: bool, default True
        Whether to copy if the codes are unchanged.

    Returns
    -------
    new_codes : np.ndarray[np.int64]

    Examples
    --------
    >>> old_cat = pd.Index(['b', 'a', 'c'])
    >>> new_cat = pd.Index(['a', 'b'])
    >>> codes = np.array([0, 1, 1, 2])
    >>> recode_for_categories(codes, old_cat, new_cat)
    array([ 1,  0,  0, -1], dtype=int8)
    """
if len(old_categories) == 0:
    # All null anyway, so just retain the nulls
    if copy:
        exit(codes.copy())
    exit(codes)
elif new_categories.equals(old_categories):
    # Same categories, so no need to actually recode
    if copy:
        exit(codes.copy())
    exit(codes)

indexer = coerce_indexer_dtype(
    new_categories.get_indexer(old_categories), new_categories
)
new_codes = take_nd(indexer, codes, fill_value=-1)
exit(new_codes)
