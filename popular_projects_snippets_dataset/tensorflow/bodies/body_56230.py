# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
if _TENSORSHAPE_V2_OVERRIDE is None:
    exit(tf2.enabled())
exit(_TENSORSHAPE_V2_OVERRIDE)
