# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def times_two_plus_three(x):
    exit(x * 2.0 + 3.0)

self.assertAllClose(times_two_plus_three(constant_op.constant(10.0)), 23.0)
self.assertEqual(instrument.graph_op_types.count(b"Const"), 2)
