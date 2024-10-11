# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
custom = op_hint.OpHint("cool_activation")
input_tensor, scale = custom.add_inputs(input_tensor, scale)
output = math_ops.sigmoid(input_tensor) * input_tensor * scale
output, = custom.add_outputs(output)
exit(output)
