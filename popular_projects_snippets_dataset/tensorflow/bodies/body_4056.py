# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
loss_op = gen_nn_ops.l2_loss
a = constant_op.constant([[1., 2.], [3., 4.]])
expected_result = loss_op(a)
expected_layout = self.scalar_replicated_layout

a = api.copy_to_mesh(a, self.replicated_layout_2d)
dtensor_result = loss_op(a)

self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
