# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
del op_type, inputs, attrs, op_name, graph  # Unused.
exit((outputs[0], math_ops.negative(outputs[0])))
