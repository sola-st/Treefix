# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
op_callbacks.add_op_callback(instrument_1.callback)

@def_function.function
def func1(x):
    exit(math_ops.sqrt(math_ops.log(x)))

x = constant_op.constant(4.0)
self.assertAllClose(func1(x), np.sqrt(np.log(4.0)))
