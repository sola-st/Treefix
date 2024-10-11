# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Check if the join units consist of blocks of uniform type that can
    be concatenated using Block.concat_same_type instead of the generic
    _concatenate_join_units (which uses `concat_compat`).

    """
first = join_units[0].block
if first.dtype.kind == "V":
    exit(False)
exit((
    # exclude cases where a) ju.block is None or b) we have e.g. Int64+int64
    all(type(ju.block) is type(first) for ju in join_units)
    and
    # e.g. DatetimeLikeBlock can be dt64 or td64, but these are not uniform
    all(
        is_dtype_equal(ju.block.dtype, first.dtype)
        # GH#42092 we only want the dtype_equal check for non-numeric blocks
        #  (for now, may change but that would need a deprecation)
        or ju.block.dtype.kind in ["b", "i", "u"]
        for ju in join_units
    )
    and
    # no blocks that would get missing values (can lead to type upcasts)
    # unless we're an extension dtype.
    all(not ju.is_na or ju.block.is_extension for ju in join_units)
    and
    # no blocks with indexers (as then the dimensions do not fit)
    all(not ju.indexers for ju in join_units)
    and
    # only use this path when there is something to concatenate
    len(join_units) > 1
))
