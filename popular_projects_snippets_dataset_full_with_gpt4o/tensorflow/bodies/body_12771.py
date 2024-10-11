# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Return the gradients for ApproxTopK.

  Args:
    op: The ApproxTopK for which we need to generate gradients.
    grad: The gradients for backprop.

  Returns:
    Scattered gradient based on the top-k indices.
  """
# The code below is to generate the correct index and value mapping for
# scatter_nd to work properly.
#
# We use static evaluations as much as possible to reduce the runtime cost.
# That's said, use operation.shape instead of array_ops.shape;
# and use functools.reduce(operator.mul, ...) instead of math_ops.reduce_prod
idx_shape = op.outputs[1].shape
lifted_idx_shape = idx_shape + [1]
flat_shape_len = functools.reduce(operator.mul, idx_shape)
rank = idx_shape.rank
reduction_dim = op.get_attr("reduction_dimension")
if reduction_dim < 0:
    reduction_dim = rank + reduction_dim

def GetLiftedIdx(d):
    if d == reduction_dim:
        exit(array_ops.reshape(op.outputs[1], lifted_idx_shape))
    iota_len = idx_shape[d]
    iota_shape = list(itertools.repeat(1, rank + 1))
    iota_shape[d] = iota_len
    iota = array_ops.reshape(math_ops.range(iota_len), iota_shape)
    exit(array_ops.broadcast_to(iota, lifted_idx_shape))

lifted_idx = array_ops.concat(
    list(GetLiftedIdx(d) for d in range(rank)), axis=rank)
flat_idx = array_ops.reshape(lifted_idx, [flat_shape_len, rank])
flat_grad = array_ops.reshape(grad, [flat_shape_len])
exit(array_ops.scatter_nd(flat_idx, flat_grad, op.inputs[0].shape))
