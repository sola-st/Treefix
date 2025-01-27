# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
value = np.ones(shape=(2, 3, 4, 5), dtype=np.float32)
expected_result = gen_nn_ops.bias_add_grad(
    out_backprop=value, data_format=data_format)

if shard_type == 'replicated':
    layout = Layout.replicated(self.mesh, rank=4)
else:
    layout = Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=4)
expected_layout = self.replicated_layout_1d

value = numpy_util.pack_numpy(value, layout)
dtensor_result = gen_nn_ops.bias_add_grad(
    out_backprop=value, data_format=data_format)
self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
