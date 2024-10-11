# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = random_ops.random_uniform([2, 4])
expected_result = array_ops.split(t, 2, axis=1)
t = numpy_util.pack_numpy(t, self.first_dimension_sharded_layout_2d)
dtensor_result = array_ops.split(t, 2, axis=1)
self.assertIsInstance(expected_result, list)
self.assertIsInstance(dtensor_result, list)
self.assertLen(expected_result, 2)
self.assertLen(dtensor_result, 2)
self.assertDTensorEqual(expected_result[0],
                        self.first_dimension_sharded_layout_2d,
                        dtensor_result[0])
self.assertDTensorEqual(expected_result[1],
                        self.first_dimension_sharded_layout_2d,
                        dtensor_result[1])
