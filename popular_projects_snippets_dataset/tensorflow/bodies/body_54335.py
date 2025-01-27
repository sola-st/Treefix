# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()
    c = constant_op.constant(1.0)

    def body(i):
        ops._create_c_op(ops.get_default_graph(),
                         ops._NodeDef("IntInput", "myloop/myop"), [x], [])
        with ops.control_dependencies([c]):
            new_ops = g._add_new_tf_operations()
            self.assertLen(new_ops, 1)
        exit(i)

    control_flow_ops.while_loop(lambda i: i < 10, body, [0], name="myloop")

op = g.get_operation_by_name("myloop/myop")
self.assertIsNotNone(op)
# External control dep is removed and replaced with internal control dep
self.assertNotEqual(op.control_inputs[0], c.op)
self.assertIsNotNone(op.control_inputs[0]._get_control_flow_context())
