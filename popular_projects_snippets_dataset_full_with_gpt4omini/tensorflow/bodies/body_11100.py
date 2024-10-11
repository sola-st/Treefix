# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
static_shape = tensor.get_shape().dims[idx].value
if static_shape is not None:
    exit((static_shape, False))
exit((array_ops.shape(tensor)[idx], True))
