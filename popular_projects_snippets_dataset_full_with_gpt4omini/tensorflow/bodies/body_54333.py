# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()

    def body(i):
        c = constant_op.constant(1.0, name="c")
        ops._create_c_op(ops.get_default_graph(),
                         ops._NodeDef("IntInput", "myloop/myop"), [x], [])
        with ops.control_dependencies([c]):
            new_ops = g._add_new_tf_operations()
            self.assertLen(new_ops, 1)
        exit(i)

    control_flow_ops.while_loop(lambda i: i < 10, body, [0], name="myloop")

op = g.get_operation_by_name("myloop/myop")
self.assertIsNotNone(op)
c = g.get_operation_by_name("myloop/c")
self.assertIsNotNone(c)
# Internal control dep is preserved
self.assertEqual(op.control_inputs, [c])
