# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
m = constant_op.constant([[1.0, -1.0], [0.0, 1.0]])
x = constant_op.constant([[-2.0], [3.0]])
op_callbacks.add_op_callback(instrument.callback)
y = math_ops.matmul(m, x, transpose_a=True, transpose_b=False)
self.assertAllClose(y, [[-2.0], [5.0]])

self.assertEqual(len(instrument.eager_attrs), 1)
self.assertIsInstance(instrument.eager_attrs[0], tuple)
self.assertEqual(
    instrument.eager_attrs[0][instrument.eager_attrs[0].index("transpose_a")
                              + 1], True)
self.assertEqual(
    instrument.eager_attrs[0][instrument.eager_attrs[0].index("transpose_b")
                              + 1], False)
self.assertEqual(len(instrument.graph_attrs), 0)
