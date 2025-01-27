# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
expected_result = array_ops.slice(t, [0, 0], [size, 2])
sharded_layout = self.first_dimension_sharded_layout

t = numpy_util.pack_numpy(t, sharded_layout)
with api.run_on(self.mesh):
    dtensor_result = array_ops.slice(t, [0, 0], [size, 2])

self.assertDTensorEqual(expected_result, sharded_layout, dtensor_result)
