# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
if data_format == 'N...C':
    c_dim = 3
    input_sharding = [
        layout_lib.UNSHARDED, layout_lib.UNSHARDED, 'y', c_dim_sharding
    ]
    a = np.ones(shape=(1, 1, 4, 4), dtype=np.float32)
    layout = Layout(input_sharding, self.mesh)
else:
    c_dim = 1
    input_sharding = [
        layout_lib.UNSHARDED, c_dim_sharding, 'y', layout_lib.UNSHARDED
    ]
    a = np.ones(shape=(1, 4, 4, 1), dtype=np.float32)
    layout = Layout(input_sharding, self.mesh)

bias = np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32)
expected_result = nn_ops.bias_add(a, bias, data_format=data_format)
expected_result_sharding = input_sharding
if c_dim_sharding == layout_lib.UNSHARDED and bias_sharding != 'y':
    expected_result_sharding[c_dim] = bias_sharding

expected_layout = Layout(expected_result_sharding, self.mesh)
a = numpy_util.pack_numpy(a, layout)
bias = numpy_util.pack_numpy(bias, Layout([bias_sharding], self.mesh))
result = nn_ops.bias_add(a, bias=bias, data_format=data_format)

self.assertDTensorEqual(expected_result, expected_layout, result)
