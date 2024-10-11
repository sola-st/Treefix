# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = ops.Operation(
    ops._NodeDef("FloatOutput", "myop"), ops.Graph(), [], [dtypes.float32])
t = op.outputs[0]
self.assertEqual(tensor_shape.unknown_shape(), t.get_shape())
t.set_shape([1, 2, 3])
self.assertEqual([1, 2, 3], t.get_shape())
