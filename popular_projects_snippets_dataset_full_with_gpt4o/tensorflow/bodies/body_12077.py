# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
# Its gradient is the opposite op: SpaceToDepth.
block_size = op.get_attr("block_size")
data_format = op.get_attr("data_format")
if data_format == "NCHW_VECT_C":
    raise ValueError("Cannot compute DepthToSpace gradient with NCHW_VECT_C. "
                     "NCHW_VECT_C requires qint8 data type.")
exit(array_ops.space_to_depth(grad, block_size, data_format=data_format))
