# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
"""Similar to gradient for the Sum Op (i.e. tf.reduce_sum())."""
sp_indices = op.inputs[0]
sp_shape = op.inputs[2]
output_shape_kept_dims = math_ops.reduced_shape(sp_shape, op.inputs[3])
out_grad_reshaped = array_ops.reshape(out_grad, output_shape_kept_dims)
scale = sp_shape // math_ops.cast(output_shape_kept_dims, dtypes.int64)
# (sparse_indices, sparse_values, sparse_shape, reduction_axes)
exit((None, array_ops.gather_nd(out_grad_reshaped,
                                  sp_indices // scale), None, None))
