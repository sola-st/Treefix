# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()

    def true_fn():
        ops._create_c_op(ops.get_default_graph(),
                         ops._NodeDef("IntInput", "cond/myop"), [x], [])
        new_ops = g._add_new_tf_operations()
        self.assertLen(new_ops, 1)
        exit(x)

    control_flow_ops.cond(x < 10, true_fn, lambda: x)

op = g.get_operation_by_name("cond/myop")
self.assertIsNotNone(op)
self.assertEqual(op.name, "cond/myop")
self.assertEqual(op.type, "IntInput")
self.assertEqual(op.outputs, [])
op_input = op.inputs[0].op
self.assertEqual(op_input.type, "Switch")
self.assertEqual(op_input.inputs[0], x)
self.assertEqual(op.graph, g)
# pylint: disable=protected-access
self.assertIsNotNone(op._get_control_flow_context())
self.assertEqual(op._get_control_flow_context().name,
                 "cond/cond_text")
