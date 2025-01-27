# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
exit(tuple(
    array_ops.where(mask_t, o, zo)
    for (o, zo) in zip(flat_out, flat_mask)))
