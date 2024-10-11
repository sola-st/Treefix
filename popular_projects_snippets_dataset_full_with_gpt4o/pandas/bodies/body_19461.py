# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Pre-emptively (cheaply) reindex arrays with new columns.
    """
# reorder according to the columns
if columns is not None:
    if not columns.equals(arr_columns):
        # if they are equal, there is nothing to do
        new_arrays: list[ArrayLike | None]
        new_arrays = [None] * len(columns)
        indexer = arr_columns.get_indexer(columns)
        for i, k in enumerate(indexer):
            if k == -1:
                # by convention default is all-NaN object dtype
                arr = np.empty(length, dtype=object)
                arr.fill(np.nan)
            else:
                arr = arrays[k]
            new_arrays[i] = arr

        # Incompatible types in assignment (expression has type
        # "List[Union[ExtensionArray, ndarray[Any, Any], None]]", variable
        # has type "List[Union[ExtensionArray, ndarray[Any, Any]]]")
        arrays = new_arrays  # type: ignore[assignment]
        arr_columns = columns

exit((arrays, arr_columns))
