# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
# TODO(b/193471732): Tracking the work to do int32 all-concat.
#
# Currently, the test will fail with segfault.
self.skipForDeviceType(['GPU'],
                       'GPUs do not support int32 StridedSliceXXX Ops')
self.skipForDeviceType(['TPU'],
                       'This test only needs to run on 2 cores.',
                       unless_device_count_equals_to=2)

a = constant_op.constant(np.array([[1, 2], [3, 4]]), dtype=dtypes.int32)
sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
unsharded_a = api.relayout(sharded_a, self.fully_replicated_layout_2d)

self.assertDTensorEqual(a, self.fully_replicated_layout_2d, unsharded_a)
