# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    c_op = ops._create_c_op(g, ops._NodeDef("IntOutput", "myop"), [], [])
    c_op2 = ops._create_c_op(g, ops._NodeDef("IntOutput", "myop_1"), [], [])
    op = g._create_op_from_tf_operation(c_op)
    op2 = g._create_op_from_tf_operation(c_op2)

    # Create ops with same names as op1 and op2. We expect the new names to be
    # uniquified.
    op3 = test_ops.int_output(name="myop").op
    op4 = test_ops.int_output(name="myop_1").op

self.assertEqual(op.name, "myop")
self.assertEqual(op2.name, "myop_1")
self.assertEqual(op3.name, "myop_2")
self.assertEqual(op4.name, "myop_1_1")
