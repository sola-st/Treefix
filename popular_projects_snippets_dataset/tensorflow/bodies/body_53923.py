# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
x = constant_op.constant(6.0)
op_callbacks.add_op_callback(instrument_1.callback)
y = math_ops.square(math_ops.log(x))
op_callbacks.remove_op_callback(instrument_1.callback)
exit(y)
