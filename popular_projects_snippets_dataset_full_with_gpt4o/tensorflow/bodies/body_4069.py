# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
input_tensor = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
shape = input_tensor.shape.as_list()
input_layout = Layout(input_layout, self.mesh)
if expected_layout is None:
    expected_layout = input_layout
else:
    expected_layout = Layout(expected_layout, self.mesh)

grad = gen_array_ops.strided_slice(input=input_tensor, **args)
expected_result = gen_array_ops.strided_slice_grad(
    shape=shape, **args, dy=grad)

dtensor_input_tensor = numpy_util.pack_numpy(input_tensor, input_layout)
grad = gen_array_ops.strided_slice(input=dtensor_input_tensor, **args)
dtensor_result = gen_array_ops.strided_slice_grad(
    shape=shape, **args, dy=grad)

self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
