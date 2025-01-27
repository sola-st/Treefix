# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
self.skipForDeviceType(['TPU'],
                       'This test only needs to run on 2 cores.',
                       unless_device_count_equals_to=2)

a = constant_op.constant(
    np.array([[1., 2., 3., 4.], [5.0, 6.0, 7.0, 8.0]]),
    dtype=dtypes.float32)
expected_result = a

sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
dtensor_result = api.relayout(sharded_a, self.fully_replicated_layout_2d)

self.assertDTensorEqual(expected_result, self.fully_replicated_layout_2d,
                        dtensor_result)
