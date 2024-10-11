# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

@def_function.function
def log_2plus_unique_x(x):
    op_callbacks.add_op_callback(instrument.callback)
    unique_values, _ = array_ops.unique(x)
    y = math_ops.log(2.0 + unique_values)
    op_callbacks.remove_op_callback(instrument.callback)
    exit(math_ops.sin(y))

x = constant_op.constant([-1.0, -1.0, 0.0], dtype=dtypes.float32)
output = log_2plus_unique_x(x)
self.assertAllClose(output, np.sin([0.0, np.log(2.0)]))

# The following ops should have been captured by the callback
# because they were constructed within the scope of `op_callback()`.
self.assertIn(_UNIQUE_OP, instrument.graph_op_types)
self.assertIn(_ADD_OP, instrument.graph_op_types)
self.assertIn(_LOG_OP, instrument.graph_op_types)
# The "Sin" op should not have been captured, because it was constructed
# outside the scope of `op_callback()`.
self.assertNotIn(_SIN_OP, instrument.graph_op_types)
self.assertEqual(
    len(instrument.graph_op_names), len(instrument.graph_op_types))

# Check the graph internal ndarrays recorded at runtime.
unique_op_outputs = instrument.graph_internal_ndarrays[_UNIQUE_OP]
self.assertEqual(len(unique_op_outputs), 2)
self.assertAllClose(unique_op_outputs[0], [-1.0, 0.0])
self.assertAllClose(unique_op_outputs[1], [0, 0, 1])
add_op_outputs = instrument.graph_internal_ndarrays[b"add"]
self.assertEqual(len(add_op_outputs), 1)
self.assertAllClose(add_op_outputs[0], [1.0, 2.0])
log_op_outputs = instrument.graph_internal_ndarrays[_LOG_OP]
self.assertEqual(len(log_op_outputs), 1)
self.assertAllClose(log_op_outputs[0], [0.0, np.log(2.0)])
