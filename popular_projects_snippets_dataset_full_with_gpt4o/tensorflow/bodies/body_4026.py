# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
value = np.ones(shape=(6, 2, 4, 2), dtype=np.float32)
bias = np.array([0.1, 0.2], dtype=np.float32)
expected_result = nn_ops.bias_add(value, bias, data_format=data_format)

if shard_type == 'replicated':
    layout = Layout.replicated(self.mesh, rank=4)
else:
    layout = Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=4)

value = numpy_util.pack_numpy(value, layout)
bias = numpy_util.pack_numpy(bias, self.replicated_layout_1d)

dtensor_result = nn_ops.bias_add(value, bias, data_format=data_format)
self.assertDTensorEqual(expected_result, layout, dtensor_result)
