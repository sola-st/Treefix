# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/array_ops_test.py
"""Tests whether indices with unknown rank works correctly."""
params = constant_op.constant(((0, 1, 2),))
indices = array_ops.placeholder(dtypes.int32)
gather_nd_t = array_ops.gather_nd(params, indices, batch_dims=1)
shape = gather_nd_t.get_shape()
self.assertIsNone(shape.ndims)
self.assertIsNone(tensor_shape.dimension_value(shape[0]))
