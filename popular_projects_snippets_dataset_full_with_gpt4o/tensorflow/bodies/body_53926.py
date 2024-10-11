# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

@def_function.function
def square_log(x):
    exit(math_ops.square(math_ops.log(x)))

# Call the function once, so that the graph construction won't show up
# in the callback.
x_float32 = constant_op.constant(6.0, dtype=dtypes.float32)
x_float64 = constant_op.constant(6.0, dtype=dtypes.float64)
square_log(x_float32)
square_log(x_float64)

op_callbacks.add_op_callback(instrument.callback)
y = square_log(x_float32)
self.assertAllClose(y, np.square(np.log(6.0)))
y = square_log(x_float64)
self.assertAllClose(y, np.square(np.log(6.0)))

self.assertEqual(instrument.eager_op_names, [None, None])
self.assertFalse(instrument.graph_op_types)
self.assertFalse(instrument.graph_op_names)
self.assertFalse(instrument.graph_inputs)

# Each of the two dtypes should be associated with its own FuncGraph.
self.assertIn(
    square_log.get_concrete_function(x_float32).name,
    instrument.eager_op_types)
self.assertIn(
    square_log.get_concrete_function(x_float64).name,
    instrument.eager_op_types)

self.assertEqual(len(instrument.eager_inputs), 2)
self.assertIsInstance(instrument.eager_inputs[0], tuple)
self.assertEqual(instrument.eager_inputs[0][0], x_float32)
self.assertIsInstance(instrument.eager_inputs[1], tuple)
self.assertEqual(instrument.eager_inputs[1][0], x_float64)
