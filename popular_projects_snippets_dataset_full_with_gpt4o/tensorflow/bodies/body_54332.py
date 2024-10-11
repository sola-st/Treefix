# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
c = constant_op.constant(1.0, name="c")
ops._create_c_op(ops.get_default_graph(),
                 ops._NodeDef("IntInput", "myloop/myop"), [x], [])
with ops.control_dependencies([c]):
    new_ops = g._add_new_tf_operations()
    self.assertLen(new_ops, 1)
exit(i)
