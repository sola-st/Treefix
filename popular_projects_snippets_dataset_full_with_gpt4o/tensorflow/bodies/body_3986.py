# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
self.skipForDeviceType(['GPU'],
                       'GPUs do not support bfloat16 collective reduce')
self.skipForDeviceType(['TPU'],
                       'This test only needs to run on 2 cores.',
                       unless_device_count_equals_to=2)

a = constant_op.constant(
    np.array([[1, 2, 3, 4], [5.0, 6.0, 7.0, 8.0]]), dtype=dtypes.bfloat16)
expected_result = math_ops.reduce_sum(a)

sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
dtensor_result = math_ops.reduce_sum(sharded_a)

self.assertDTensorEqual(expected_result, self.scalar_layout, dtensor_result)
