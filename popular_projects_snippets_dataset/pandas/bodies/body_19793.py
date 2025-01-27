# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
exit((
    # TODO: should this be ju.block._can_hold_na?
    all(ju.block.is_extension for ju in join_units)
    and len({ju.block.dtype.name for ju in join_units}) == 1
))
