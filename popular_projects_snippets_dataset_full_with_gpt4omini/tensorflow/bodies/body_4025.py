# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
value = np.array([[1., 2.], [3., 4.]])
bias = np.array([0.1, 0.2])
expected_result = nn_ops.bias_add(value, bias)

if shard_type == 'replicated':
    layout = self.replicated_layout_2d
else:
    layout = self.first_dimension_sharded_layout

value = numpy_util.pack_numpy(value, layout)
bias = numpy_util.pack_numpy(bias, self.replicated_layout_1d)
dtensor_result = nn_ops.bias_add(value, bias)
self.assertDTensorEqual(expected_result, layout, dtensor_result)
