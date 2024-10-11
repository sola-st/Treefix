# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant(
    np.array([[1., 2.], [3., 4.], [5.0, 6.0], [7.0, 8.0]]),
    dtype=dtypes.float32)
expected_result = math_ops.reduce_logsumexp(a, axis=-1)

a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout)

with api.run_on(self.mesh):
    dtensor_result = math_ops.reduce_logsumexp(a, axis=-1)

    self.assertDTensorEqual(expected_result,
                            self.first_dimension_sharded_layout_1d,
                            dtensor_result)
