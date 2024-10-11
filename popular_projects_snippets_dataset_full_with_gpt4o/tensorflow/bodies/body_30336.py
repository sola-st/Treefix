# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
params = constant_op.constant([[0, 1, 2]])
indices = array_ops.placeholder(dtypes.int32)
gather_nd_t = array_ops.gather_nd(params, indices)
shape = gather_nd_t.get_shape()
self.assertEqual(None, shape.ndims)
self.assertEqual(None, tensor_shape.dimension_value(shape[0]))
