# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
expected_result = array_ops.unstack(t, axis=0)
t = api.copy_to_mesh(t, self.replicated_layout_2d)
dtensor_result = array_ops.unstack(t, axis=0)
self.assertIsInstance(expected_result, list)
self.assertIsInstance(dtensor_result, list)
self.assertLen(expected_result, 2)
self.assertLen(dtensor_result, 2)
self.assertDTensorEqual(expected_result[0], self.replicated_layout_1d,
                        dtensor_result[0])
self.assertDTensorEqual(expected_result[1], self.replicated_layout_1d,
                        dtensor_result[1])
