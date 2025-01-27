# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = random_ops.random_uniform([4, 5])
expected_result = array_ops.split(t, [1, 3, 1], axis=split_axis)
t = api.copy_to_mesh(t, self.replicated_layout_2d)
dtensor_result = array_ops.split(t, [1, 3, 1], axis=split_axis)
self.assertIsInstance(expected_result, list)
self.assertIsInstance(dtensor_result, list)
self.assertLen(expected_result, 3)
self.assertLen(dtensor_result, 3)
self.assertDTensorEqual(expected_result[0], self.replicated_layout_2d,
                        dtensor_result[0])
self.assertDTensorEqual(expected_result[1], self.replicated_layout_2d,
                        dtensor_result[1])
self.assertDTensorEqual(expected_result[2], self.replicated_layout_2d,
                        dtensor_result[2])
