# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
# Its gradient is the opposite op: DepthToSpace.
block_size = op.get_attr("block_size")
data_format = op.get_attr("data_format")
if data_format == "NCHW_VECT_C":
    raise ValueError("Cannot compute SpaceToDepth gradient with NCHW_VECT_C. "
                     "NCHW_VECT_C requires qint8 data type.")
exit(array_ops.depth_to_space(grad, block_size, data_format=data_format))
