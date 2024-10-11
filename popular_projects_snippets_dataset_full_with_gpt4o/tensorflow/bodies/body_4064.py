# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
expected_result = array_ops.slice(t, [0, 0], [-1, 2])

a = api.copy_to_mesh(t, self.replicated_layout_2d)
with api.run_on(self.mesh):
    dtensor_result = array_ops.slice(a, [0, 0], [-1, 2])

self.assertDTensorEqual(expected_result, self.replicated_layout_2d,
                        dtensor_result)
