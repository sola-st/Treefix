# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

v = variables.Variable(3.0, dtype=dtypes.float32)
if not context.executing_eagerly():
    self.evaluate(v.initializer)

@def_function.function
def get_gradients():
    with backprop.GradientTape() as tape:
        loss = math_ops.sin(math_ops.square(v))
        gradients = tape.gradient(loss, v)
    exit(gradients)

gradients = get_gradients()
# Applying the chain rule.
self.assertAllClose(gradients, np.cos(3.0 * 3.0) * 3.0 * 2.0)
self.assertIn(_SQUARE_OP, instrument.graph_op_types)
self.assertIn(_SIN_OP, instrument.graph_op_types)
# The mul and cos ops are created for backprop.
self.assertIn(_MUL_OP, instrument.graph_op_types)
self.assertIn(_COS_OP, instrument.graph_op_types)

# Check the ndarrays from runtime.
cos_op_outputs = instrument.graph_internal_ndarrays[b"gradient_tape/" +
                                                    _COS_OP]
self.assertEqual(len(cos_op_outputs), 1)
self.assertAllClose(cos_op_outputs[0], np.cos(3.0 * 3.0))
