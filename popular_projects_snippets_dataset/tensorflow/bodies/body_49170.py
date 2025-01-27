# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
tiled_mask_t = tuple(
    _expand_mask(mask_t, o, fixed_dim=len(mask_t.shape))
    for o in flat_out)
exit(tuple(
    array_ops.where_v2(m, o, fm)
    for m, o, fm in zip(tiled_mask_t, flat_out, flat_mask)))
