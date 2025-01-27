# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# tuples produced within _form_blocks are of the form (placement, array)
exit([
    new_block_2d(ensure_block_shape(x[1], ndim=2), placement=BlockPlacement(x[0]))
    for x in tuples
])
