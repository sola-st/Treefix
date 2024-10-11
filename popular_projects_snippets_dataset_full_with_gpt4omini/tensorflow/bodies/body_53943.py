# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

@def_function.function
def my_matmul(m, x):
    exit(math_ops.matmul(m, x, transpose_a=True, transpose_b=False))

m = constant_op.constant([[1.0, -1.0], [0.0, 1.0]])
x = constant_op.constant([[-2.0], [3.0]])
op_callbacks.add_op_callback(instrument.callback)
y = my_matmul(m, x)
self.assertAllClose(y, [[-2.0], [5.0]])

index = instrument.graph_op_types.index(_MATMUL_OP)
self.assertIsInstance(instrument.graph_attrs[index], tuple)
self.assertEqual(
    instrument.graph_attrs[index][
        instrument.graph_attrs[index].index("transpose_a") + 1].b, True)
self.assertEqual(
    instrument.graph_attrs[index][
        instrument.graph_attrs[index].index("transpose_b") + 1].b, False)
if context.executing_eagerly():
    self.assertEqual(len(instrument.eager_attrs), 1)
    self.assertIsInstance(instrument.eager_attrs[0], tuple)
