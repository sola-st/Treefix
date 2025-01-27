# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

x = constant_op.constant(6.0)
op_callbacks.add_op_callback(instrument.callback)
y = math_ops.square(math_ops.log(x))
self.assertAllClose(y, np.square(np.log(6.0)))

self.assertEqual(instrument.eager_op_types, [_LOG_OP, _SQUARE_OP])
# Op names are unavailable under eager mode.
self.assertEqual(instrument.eager_op_names, [None, None])
self.assertEqual(instrument.eager_graphs, [None, None])
self.assertEqual(len(instrument.eager_inputs), 2)
self.assertEqual(len(instrument.eager_inputs[0]), 1)
self.assertIsInstance(instrument.eager_inputs[0], tuple)
self.assertEqual(instrument.eager_inputs[0][0], x)
self.assertEqual(len(instrument.eager_inputs[1]), 1)
self.assertIsInstance(instrument.eager_inputs[1], tuple)
self.assertAllClose(instrument.eager_inputs[1][0], np.log(6.0))
self.assertFalse(instrument.graph_op_types)
self.assertFalse(instrument.graph_op_names)
self.assertFalse(instrument.graph_attrs)
self.assertFalse(instrument.graph_graphs)
self.assertFalse(instrument.graph_inputs)
