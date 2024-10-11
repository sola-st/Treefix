# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaisesOpError(msg):
    with ops.Graph().as_default():
        node_def = ops._NodeDef("IntOutput", "name")
        node_def_orig = ops._NodeDef("IntOutput", "orig")
        op_orig = ops.Operation(node_def_orig, ops.get_default_graph())
        op = ops.Operation(node_def, ops.get_default_graph(),
                           original_op=op_orig)
        raise errors.UnauthenticatedError(node_def, op, "true_err")
