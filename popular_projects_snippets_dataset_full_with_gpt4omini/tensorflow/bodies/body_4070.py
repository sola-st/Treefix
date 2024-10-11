# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU'], 'b/123559667; op has no XLA implementation')
input_tensor = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
value_tensor = gen_array_ops.strided_slice(input=input_tensor, **args) * 10.
expected_result = gen_array_ops.tensor_strided_slice_update(
    input=input_tensor, value=value_tensor, **args)

input_layout = Layout(input_layout, self.mesh)
value_layout = Layout(value_layout, self.mesh)
if expected_layout is None:
    expected_layout = input_layout
else:
    expected_layout = Layout(expected_layout, self.mesh)

dtensor_input_tensor = numpy_util.pack_numpy(input_tensor, input_layout)
dtensor_value_tensor = numpy_util.pack_numpy(value_tensor, value_layout)
dtensor_result = gen_array_ops.tensor_strided_slice_update(
    input=dtensor_input_tensor, value=dtensor_value_tensor, **args)

self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
