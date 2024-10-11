# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
if cast_to_f32:
    tensor = math_ops.cast(tensor, dtypes.float32)
output_tensor = tf_op(tensor)
# Return type should be scalar. Set it if it does not have the
# information.
if not output_tensor.get_shape().is_fully_defined():
    output_tensor = array_ops.reshape(output_tensor, [])
exit(output_tensor)
