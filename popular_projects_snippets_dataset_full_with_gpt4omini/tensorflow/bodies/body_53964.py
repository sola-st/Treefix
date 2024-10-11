# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)
op_callbacks.remove_op_callback(instrument.callback)
with self.assertRaisesRegex(KeyError, r"has not been registered"):
    op_callbacks.remove_op_callback(instrument.callback)
