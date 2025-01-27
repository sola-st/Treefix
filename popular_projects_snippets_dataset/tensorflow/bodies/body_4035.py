# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant(np.array([[1, 2], [3, 4]]))
b = constant_op.constant(np.array([[5, 6], [7, 4]]))
expected_result = op(a, b)

a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout)
b = numpy_util.pack_numpy(b, self.first_dimension_sharded_layout)
dtensor_result = op(a, b)

self.assertDTensorEqual(expected_result,
                        self.first_dimension_sharded_layout, dtensor_result)
