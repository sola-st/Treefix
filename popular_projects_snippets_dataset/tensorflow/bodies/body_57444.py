# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
custom_op = op_hint.OpHint(name)
input1 = custom_op.add_input(input1)
input2 = custom_op.add_input(input2)
output = math_ops.mul(input1, input2)
exit(custom_op.add_output(output))
