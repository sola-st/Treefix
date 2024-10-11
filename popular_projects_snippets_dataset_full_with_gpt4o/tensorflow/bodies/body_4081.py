# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU'], 'waiting for cl/344197900')
num_segments = 12
data = np.random.uniform(size=[num_segments, 4])
segment_ids = np.random.randint(0, num_segments, size=num_segments)
expected = gen_math_ops.unsorted_segment_sum(data, segment_ids,
                                             num_segments)

data = numpy_util.pack_numpy(data, Layout.replicated(self.mesh, 2))
segment_ids = numpy_util.pack_numpy(
    segment_ids, Layout.batch_sharded(self.mesh, _MESH_DIM_Y, rank=1))
with api.run_on(self.mesh):
    dtensor_result = gen_math_ops.unsorted_segment_sum(
        data, segment_ids, num_segments)
    expected_layout = Layout.replicated(self.mesh, 2)
    self.assertDTensorEqual(expected, expected_layout, dtensor_result)
