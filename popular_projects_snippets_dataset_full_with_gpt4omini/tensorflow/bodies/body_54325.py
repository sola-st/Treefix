# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()
    c_op = ops._create_c_op(
        g, ops._NodeDef("IntInputIntOutput", "myop"), [x], [])
    op = g._create_op_from_tf_operation(c_op)

self.assertEqual(op.name, "myop")
self.assertEqual(op.type, "IntInputIntOutput")
self.assertLen(op.outputs, 1)
self.assertEqual(op.outputs[0].shape, tensor_shape.unknown_shape())
self.assertEqual(list(op.inputs), [x])
self.assertEqual(op.control_inputs, [])
self.assertEqual(op.graph, g)
self.assertEqual(x.consumers(), [op])
self.assertIsNotNone(op.traceback)
self.assertIn("testBasic", op.traceback[-1])
self.assertEqual(g.get_operation_by_name("myop"), op)
self.assertEqual(g.get_tensor_by_name("myop:0"), op.outputs[0])
