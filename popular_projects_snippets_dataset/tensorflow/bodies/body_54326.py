# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant([[1, 2, 3], [4, 5, 6]])
    c_op = ops._create_c_op(g, ops._NodeDef("Identity", "myop"), [x], [])
    op = g._create_op_from_tf_operation(c_op)

self.assertEqual(op.name, "myop")
self.assertEqual(op.type, "Identity")
self.assertLen(op.outputs, 1)
self.assertEqual(op.outputs[0].shape, tensor_shape.TensorShape([2, 3]))
