# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Sum reduces grad along the tiled dimensions."""
input_shape = array_ops.shape(op.inputs[0], out_type=op.inputs[1].dtype)
# We interleave multiples and input_shape to get split_shape,
# reshape grad to split_shape, and reduce along all even
# dimensions (the tiled dimensions) to get the result
# with shape input_shape.  For example
#   input_shape = [20, 30, 40]
#   multiples = [2, 3, 4]
#   split_shape = [2, 20, 3, 30, 4, 40]
#   axes = [0, 2, 4]
split_shape = array_ops.reshape(
    array_ops.transpose(array_ops.stack([op.inputs[1], input_shape])), [-1])
axes = math_ops.range(0, array_ops.size(split_shape), 2)
# Sum reduces grad along the first dimension for IndexedSlices
if isinstance(grad, indexed_slices_lib.IndexedSlices):
    input_shape_0 = math_ops.cast(input_shape[0], grad.indices.dtype)
    grad = math_ops.unsorted_segment_sum(
        grad.values, math_ops.mod(grad.indices, input_shape_0), input_shape_0)
    split_shape = array_ops.concat([[1], split_shape[1:]], axis=0)
input_grad = math_ops.reduce_sum(array_ops.reshape(grad, split_shape), axes)
# Fix shape inference
if not context.executing_eagerly():
    input_grad.set_shape(op.inputs[0].get_shape())
exit([input_grad, None])
