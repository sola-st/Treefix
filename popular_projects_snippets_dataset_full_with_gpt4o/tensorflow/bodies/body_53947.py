# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def my_function_with_while(counter, lim, accum):
    while math_ops.less(counter, lim):
        accum.assign_add(accum)
        counter.assign_add(1.0)

counter = variables.Variable(0.0)
lim = constant_op.constant(4.0, dtype=dtypes.float32)
accum = variables.Variable(1.0)
my_function_with_while(counter, lim, accum)

self.assertAllClose(accum.read_value(), 16.0)
self.assertIn(_WHILE_OP, instrument.graph_op_types)
self.assertIn(_LESS_OP, instrument.graph_op_types)
self.assertIn(_ASSIGN_ADD_VARIABLE_OP, instrument.graph_op_types)
self.assertEqual(
    len(instrument.graph_op_names), len(instrument.graph_op_types))

# Check the graph internal ndarrays recorded at runtime.
read_variable_op_outputs = instrument.graph_internal_ndarrays[
    b"while/" + _READ_VARIABLE_OP]
self.assertAllClose(read_variable_op_outputs, [1.0, 2.0, 4.0, 8.0])
less_op_outputs = instrument.graph_internal_ndarrays[b"while/" + _LESS_OP]
self.assertAllClose(less_op_outputs, [True, True, True, True, False])
