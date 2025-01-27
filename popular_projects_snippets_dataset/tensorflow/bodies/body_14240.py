# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
sparse_indices, output_shape, _, _ = op.inputs

sparse_values_grad = array_ops.gather_nd(grad, sparse_indices)
default_value_grad = math_ops.reduce_sum(grad) - math_ops.reduce_sum(
    sparse_values_grad)
exit([
    array_ops.zeros_like(sparse_indices),
    array_ops.zeros_like(output_shape), sparse_values_grad, default_value_grad
])
