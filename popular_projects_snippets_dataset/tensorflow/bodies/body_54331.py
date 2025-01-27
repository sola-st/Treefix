# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()

    def body(i):
        ops._create_c_op(ops.get_default_graph(),
                         ops._NodeDef("IntInput", "myloop/myop"), [x], [])
        new_ops = g._add_new_tf_operations()
        self.assertLen(new_ops, 1)
        exit(i)

    control_flow_ops.while_loop(lambda i: i < 10, body, [0], name="myloop")

op = g.get_operation_by_name("myloop/myop")
self.assertIsNotNone(op)
self.assertEqual(op.name, "myloop/myop")
self.assertEqual(op.type, "IntInput")
self.assertEqual(op.outputs, [])
op_input = op.inputs[0].op
self.assertEqual(op_input.type, "Enter")
self.assertEqual(list(op_input.inputs), [x])
self.assertEqual(op.graph, g)
# pylint: disable=protected-access
self.assertIsNotNone(op._get_control_flow_context())
self.assertEqual(op._get_control_flow_context().name,
                 "myloop/while_context")
