# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Concatenate values from several join units along axis=1.
    """
empty_dtype = _get_empty_dtype(join_units)

has_none_blocks = any(unit.block.dtype.kind == "V" for unit in join_units)
upcasted_na = _dtype_to_na_value(empty_dtype, has_none_blocks)

to_concat = [
    ju.get_reindexed_values(empty_dtype=empty_dtype, upcasted_na=upcasted_na)
    for ju in join_units
]

if len(to_concat) == 1:
    # Only one block, nothing to concatenate.
    concat_values = to_concat[0]
    if copy:
        if isinstance(concat_values, np.ndarray):
            # non-reindexed (=not yet copied) arrays are made into a view
            # in JoinUnit.get_reindexed_values
            if concat_values.base is not None:
                concat_values = concat_values.copy()
        else:
            concat_values = concat_values.copy()

elif any(is_1d_only_ea_dtype(t.dtype) for t in to_concat):
    # TODO(EA2D): special case not needed if all EAs used HybridBlocks
    # NB: we are still assuming here that Hybrid blocks have shape (1, N)
    # concatting with at least one EA means we are concatting a single column
    # the non-EA values are 2D arrays with shape (1, n)

    # error: No overload variant of "__getitem__" of "ExtensionArray" matches
    # argument type "Tuple[int, slice]"
    to_concat = [
        t
        if is_1d_only_ea_dtype(t.dtype)
        else t[0, :]  # type: ignore[call-overload]
        for t in to_concat
    ]
    concat_values = concat_compat(to_concat, axis=0, ea_compat_axis=True)
    concat_values = ensure_block_shape(concat_values, 2)

else:
    concat_values = concat_compat(to_concat, axis=1)

exit(concat_values)
