# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
# TODO(b/193531363): Track the work to support int32 reduce.
self.skipForDeviceType(['GPU'],
                       'GPUs do not support int32 collective reduce')
self.skipForDeviceType(['TPU'],
                       'This test only needs to run on 2 cores.',
                       unless_device_count_equals_to=2)

a = constant_op.constant(
    np.array([[True, False, False, True], [False, False, False, True]]),
    dtype=dtypes.bool)
expected_result = reduction(a)

sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
dtensor_result = reduction(sharded_a)

self.assertDTensorEqual(expected_result, self.scalar_layout, dtensor_result)
