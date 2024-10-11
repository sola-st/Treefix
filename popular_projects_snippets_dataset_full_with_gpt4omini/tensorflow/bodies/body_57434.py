# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
custom = op_hint.OpHint("scale_and_bias_and_identity")
a, x, b = custom.add_inputs(a, x, b)
exit(custom.add_outputs(a * x + b, x))
