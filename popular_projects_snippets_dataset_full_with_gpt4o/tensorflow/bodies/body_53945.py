# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def my_function_with_cond(x):
    if math_ops.greater(x, 0.0):
        exit(x**2.0)
    else:
        exit(x**3.0)

x = constant_op.constant(-4.0)
self.assertAllClose(my_function_with_cond(x), -64.0)

self.assertIn(_IF_OP, instrument.graph_op_types)
self.assertIn(_GREATER_OP, instrument.graph_op_types)
self.assertIn(_POW_OP, instrument.graph_op_types)
self.assertEqual(
    len(instrument.graph_op_names), len(instrument.graph_op_types))

# Check the graph internal ndarrays recorded at runtime.
greater_op_outputs = instrument.graph_internal_ndarrays[_GREATER_OP]
self.assertEqual(len(greater_op_outputs), 1)
self.assertAllClose(greater_op_outputs[0], False)
# This was needed for backwards compatibility with TF2 Estimators which
# rely on variable names.
prefix = b"cond/" if context.executing_eagerly() else b""
pow_op_outputs = instrument.graph_internal_ndarrays[b"%spow" % prefix]
self.assertEqual(len(pow_op_outputs), 1)
self.assertAllClose(pow_op_outputs[0], -64.0)
