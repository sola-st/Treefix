# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
a = constant_op.constant(
    np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), dtype=dtypes.int32)

expected_result = math_ops.reduce_sum(a)

sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
dtensor_result = math_ops.reduce_sum(sharded_a)

self.assertDTensorEqual(expected_result, self.scalar_layout, dtensor_result)
