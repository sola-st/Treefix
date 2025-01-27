# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for Prod."""
# The gradient can be expressed by dividing the product by each entry of the
# input tensor, but this approach can't deal with zeros in the input.
# Here, we avoid this problem by composing the output as a product of two
# cumprod operations.

input_shape = array_ops.shape(op.inputs[0])
# Reshape reduction indices for the case where the parameter is a scalar
reduction_indices = array_ops.reshape(op.inputs[1], [-1])

# Expand grad to full input shape
if not op.get_attr("keep_dims"):
    output_shape_kept_dims = math_ops.reduced_shape(input_shape, op.inputs[1])
    grad = array_ops.reshape(grad, output_shape_kept_dims)

grad = array_ops.broadcast_to(grad, input_shape)

# Pack all reduced dimensions into a single one, so we can perform the
# cumprod ops. If the reduction dims list is empty, it defaults to float32,
# so we need to cast here.  We put all the shape-related ops on CPU to avoid
# copying back and forth, and since listdiff is CPU only.
with ops.device("/cpu:0"):
    rank = array_ops.rank(op.inputs[0])
    reduction_indices = (reduction_indices + rank) % rank
    reduced = math_ops.cast(reduction_indices, dtypes.int32)
    idx = math_ops.range(0, rank)
    other, _ = gen_array_ops.list_diff(idx, reduced, dtypes.int32)
    perm = array_ops.concat([reduced, other], 0)
    reduced_num = math_ops.reduce_prod(array_ops.gather(input_shape, reduced))
    other_num = math_ops.reduce_prod(array_ops.gather(input_shape, other))
permuted = array_ops.transpose(op.inputs[0], perm)
permuted_shape = array_ops.shape(permuted)
reshaped = array_ops.reshape(permuted, (reduced_num, other_num))

# Calculate product, leaving out the current entry
left = math_ops.cumprod(reshaped, axis=0, exclusive=True)
right = math_ops.cumprod(reshaped, axis=0, exclusive=True, reverse=True)
# For complex inputs, the gradient is in the conjugate direction.
y = array_ops.reshape(
    math_ops.conj(left) * math_ops.conj(right), permuted_shape)

# Invert the transpose and reshape operations.
# Make sure to set the statically known shape information through a reshape.
out = grad * array_ops.transpose(y, array_ops.invert_permutation(perm))
exit((array_ops.reshape(out, input_shape), None))
