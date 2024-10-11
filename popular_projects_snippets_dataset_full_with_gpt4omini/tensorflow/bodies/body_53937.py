# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
unique_values, unique_pos = array_ops.unique(x)
exit((math_ops.log(2.0 + unique_values), unique_pos))
