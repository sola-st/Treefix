# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def log_2plus_unique_x(x):
    unique_values, unique_pos = array_ops.unique(x)
    exit((math_ops.log(2.0 + unique_values), unique_pos))

x = constant_op.constant([-1.0, -1.0, 0.0], dtype=dtypes.float32)
y1, y2 = log_2plus_unique_x(x)
self.assertAllClose(y1, [0.0, np.log(2.0)])
self.assertAllClose(y2, [0, 0, 1])

self.assertIn(_UNIQUE_OP, instrument.graph_op_types)
self.assertIn(_ADD_OP, instrument.graph_op_types)
self.assertIn(_LOG_OP, instrument.graph_op_types)
self.assertEqual(
    len(instrument.graph_op_names), len(instrument.graph_op_types))

# Check the graph internal ndarrays recorded at runtime.
unique_op_outputs = instrument.graph_internal_ndarrays[_UNIQUE_OP]
if context.executing_eagerly():
    # b/140810696: The run_in_graph_and_eager_modes decorator runs
    # Session.run() twice. We can't assert on the number of outputs in
    # that case.
    self.assertEqual(len(unique_op_outputs), 2)
self.assertAllClose(unique_op_outputs[0], [-1.0, 0.0])
self.assertAllClose(unique_op_outputs[1], [0, 0, 1])
add_op_outputs = instrument.graph_internal_ndarrays[b"add"]
if context.executing_eagerly():
    self.assertEqual(len(add_op_outputs), 1)
self.assertAllClose(add_op_outputs[0], [1.0, 2.0])
log_op_outputs = instrument.graph_internal_ndarrays[_LOG_OP]
if context.executing_eagerly():
    self.assertEqual(len(log_op_outputs), 1)
self.assertAllClose(log_op_outputs[0], [0.0, np.log(2.0)])
