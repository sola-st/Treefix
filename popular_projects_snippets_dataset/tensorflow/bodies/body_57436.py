# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
custom = op_hint.OpHint("add_test")
x, = custom.add_inputs(x)
output = math_ops.multiply(x, x)
output, = custom.add_outputs(output)
exit(output)
