# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Segregate Series based on type and coerce into matrices.

    Needs to handle a lot of exceptional cases.
    """
if verify_integrity:
    # figure out the index, if necessary
    if index is None:
        index = _extract_index(arrays)
    else:
        index = ensure_index(index)

    # don't force copy because getting jammed in an ndarray anyway
    arrays = _homogenize(arrays, index, dtype)
    # _homogenize ensures
    #  - all(len(x) == len(index) for x in arrays)
    #  - all(x.ndim == 1 for x in arrays)
    #  - all(isinstance(x, (np.ndarray, ExtensionArray)) for x in arrays)
    #  - all(type(x) is not PandasArray for x in arrays)

else:
    index = ensure_index(index)
    arrays = [extract_array(x, extract_numpy=True) for x in arrays]

    # Reached via DataFrame._from_arrays; we do validation here
    for arr in arrays:
        if (
            not isinstance(arr, (np.ndarray, ExtensionArray))
            or arr.ndim != 1
            or len(arr) != len(index)
        ):
            raise ValueError(
                "Arrays must be 1-dimensional np.ndarray or ExtensionArray "
                "with length matching len(index)"
            )

columns = ensure_index(columns)
if len(columns) != len(arrays):
    raise ValueError("len(arrays) must match len(columns)")

# from BlockManager perspective
axes = [columns, index]

if typ == "block":
    exit(create_block_manager_from_column_arrays(
        arrays, axes, consolidate=consolidate
    ))
elif typ == "array":
    exit(ArrayManager(arrays, [index, columns]))
else:
    raise ValueError(f"'typ' needs to be one of {{'block', 'array'}}, got '{typ}'")
