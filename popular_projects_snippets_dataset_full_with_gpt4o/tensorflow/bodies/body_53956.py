# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

x = constant_op.constant(10.0)
y = constant_op.constant(20.0)
op_callbacks.add_op_callback(instrument.callback)
z = x + y
w = control_flow_ops.group([z])
self.assertIsNone(w)
self.assertEqual(instrument.eager_op_types, [_ADD_OP])
