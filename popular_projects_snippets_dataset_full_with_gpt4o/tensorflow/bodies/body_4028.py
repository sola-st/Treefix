# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
value = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
expected_result = gen_nn_ops.bias_add_grad(out_backprop=value)

if shard_type == 'replicated':
    layout = self.replicated_layout_2d
else:
    layout = self.first_dimension_sharded_layout
expected_layout = self.replicated_layout_1d

value = numpy_util.pack_numpy(value, layout)
dtensor_result = gen_nn_ops.bias_add_grad(out_backprop=value)
self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
