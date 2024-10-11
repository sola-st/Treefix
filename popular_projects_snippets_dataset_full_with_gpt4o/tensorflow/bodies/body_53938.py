# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback(instrument_graph_ops=False)

op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def log_2plus_unique_x(x):
    unique_values, unique_pos = array_ops.unique(x)
    exit((math_ops.log(2.0 + unique_values), unique_pos))

x = constant_op.constant([-1.0, -1.0, 0.0], dtype=dtypes.float32)
y1, y2 = log_2plus_unique_x(x)
self.assertAllClose(y1, [0.0, np.log(2.0)])
self.assertAllClose(y2, [0, 0, 1])

# Check the recorded input tensors.
self.assertEqual(
    len(instrument.graph_inputs), len(instrument.graph_op_types))
unique_inputs = instrument.graph_inputs[instrument.graph_op_types.index(
    _UNIQUE_OP)]
self.assertIsInstance(unique_inputs, tuple)
self.assertEqual(len(unique_inputs), 1)
self.assertEqual(
    compat.as_bytes(unique_inputs[0].op.op_def.name), _PLACEHOLDER_OP)

add_inputs = instrument.graph_inputs[instrument.graph_op_types.index(
    _ADD_OP)]
self.assertIsInstance(add_inputs, tuple)
self.assertEqual(len(add_inputs), 2)
self.assertEqual(
    compat.as_bytes(add_inputs[0].op.op_def.name), _CONSTANT_OP)
self.assertEqual(compat.as_bytes(add_inputs[1].op.op_def.name), _UNIQUE_OP)

log_inputs = instrument.graph_inputs[instrument.graph_op_types.index(
    _LOG_OP)]
self.assertIsInstance(log_inputs, tuple)
self.assertEqual(len(log_inputs), 1)
self.assertEqual(compat.as_bytes(log_inputs[0].op.op_def.name), _ADD_OP)

# Check the recorded graphs.
self.assertEqual(
    len(instrument.graph_graphs), len(instrument.graph_op_types))
self.assertGreater(len(instrument.graph_graph_versions), 1)
if context.executing_eagerly():
    for i in range(len(instrument.graph_graph_versions) - 1):
        self.assertGreater(instrument.graph_graph_versions[i + 1],
                           instrument.graph_graph_versions[i])
