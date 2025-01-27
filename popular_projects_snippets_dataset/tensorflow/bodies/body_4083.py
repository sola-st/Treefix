# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
op = gen_array_ops.broadcast_to
a = constant_op.constant([[1.], [3.]])
assert a.shape == [2, 1]

expected_result = op(a, new_shape)

a = api.copy_to_mesh(a, self.replicated_layout_2d)
dtensor_result = op(a, new_shape)

self.assertDTensorEqual(expected_result,
                        Layout.replicated(self.mesh, len(new_shape)),
                        dtensor_result)
