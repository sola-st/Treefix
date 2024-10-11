# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
ctx = context.context()
instrument_0 = _NumpyFunctionCallback()
instrument_1 = _NumpyFunctionCallback()

op_callbacks.add_op_callback(instrument_0.callback)
self.assertEqual(1, len(ctx.op_callbacks))
self.assertIn(instrument_0.callback, ctx.op_callbacks)

op_callbacks.add_op_callback(instrument_1.callback)
self.assertEqual(2, len(ctx.op_callbacks))
self.assertIn(instrument_0.callback, ctx.op_callbacks)
self.assertIn(instrument_1.callback, ctx.op_callbacks)

op_callbacks.remove_op_callback(instrument_1.callback)
self.assertEqual(1, len(ctx.op_callbacks))
self.assertIn(instrument_0.callback, ctx.op_callbacks)

op_callbacks.remove_op_callback(instrument_0.callback)
self.assertEqual(0, len(ctx.op_callbacks))
