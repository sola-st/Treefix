# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['GPU'], 'reduce on GPU only supports int64')
num_segments = 12
data = np.random.uniform(size=[num_segments, 4]).astype(np.float32)
segment_ids = np.random.randint(
    0, num_segments, size=num_segments, dtype=np.int32)
expected = gen_math_ops.unsorted_segment_sum(data, segment_ids,
                                             num_segments)

data = numpy_util.pack_numpy(
    data, Layout([layout_lib.UNSHARDED, _MESH_DIM_X], self.mesh))
segment_ids = numpy_util.pack_numpy(segment_ids,
                                    Layout.replicated(self.mesh, 1))

with api._dtensor_device()._default_layout(Layout.replicated(self.mesh, 2)):
    with api.run_on(self.mesh):
        dtensor_result = gen_math_ops.unsorted_segment_sum(
            data, segment_ids, num_segments)
        expected_layout = Layout.replicated(self.mesh, 2)
        self.assertDTensorEqual(expected, expected_layout, dtensor_result)
