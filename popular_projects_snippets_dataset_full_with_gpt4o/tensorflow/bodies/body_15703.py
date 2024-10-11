# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/strings_reduce_join_op_test.py
with self.cached_session():
    input_tensor = ragged_factory_ops.constant(input_array)
    output = ragged_string_ops.reduce_join(
        inputs=input_tensor,
        axis=axis,
        keepdims=keepdims,
        separator=separator)
    output_array = self.evaluate(output)
self.assertAllEqual(truth, output_array)
if all(isinstance(s, tensor_shape.Dimension) for s in output.shape):
    output_shape = [dim.value for dim in output.shape]
else:
    output_shape = output.shape
self.assertAllEqual(truth_shape, output_shape)
