# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['GPU'], 'b/169353279: int32 caused segfault on GPU')

axis = [1]
# Disable the pylint as the cell var is used for this iteration only.
# pylint: disable=cell-var-from-loop
reduction_op = lambda x: op(x, axis=axis)
# pylint: enable=cell-var-from-loop

a = constant_op.constant(
    np.array([[1., 2.], [3., 4.], [5.0, 6.0], [7.0, 8.0]]), dtype=dtype)
expected_result = reduction_op(a)
a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout)

with api.run_on(self.mesh):
    dtensor_result = reduction_op(a)

    self.assertDTensorEqual(expected_result,
                            self.first_dimension_sharded_layout_1d,
                            dtensor_result)
