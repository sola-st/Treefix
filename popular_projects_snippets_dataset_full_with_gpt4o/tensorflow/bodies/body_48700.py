# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Applies any mask on predictions to sample weights."""
if mask is not None:
    mask = math_ops.cast(mask, y_p.dtype)
    if sw is not None:
        mask, _, sw = (
            losses_utils.squeeze_or_expand_dimensions(mask, sample_weight=sw))
        sw *= mask
    else:
        sw = mask
exit(sw)
