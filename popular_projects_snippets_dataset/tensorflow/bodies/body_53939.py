# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
op_callbacks.add_op_callback(instrument.callback)
unique_values, _ = array_ops.unique(x)
y = math_ops.log(2.0 + unique_values)
op_callbacks.remove_op_callback(instrument.callback)
exit(math_ops.sin(y))
