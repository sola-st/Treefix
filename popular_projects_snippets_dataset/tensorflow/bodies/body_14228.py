# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
sp_indices = op.inputs[0]
# (sparse_indices, sparse_values, sparse_shape, dense)
exit((None, array_ops.gather_nd(out_grad, sp_indices), None, out_grad))
