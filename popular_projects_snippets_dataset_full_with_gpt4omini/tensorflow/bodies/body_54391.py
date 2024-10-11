# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.float_output()
    with g.gradient_override_map({"CopyOp": "unknown_override"}):
        y = test_ops.copy_op(x)
    with self.assertRaisesRegex(LookupError, "unknown_override"):
        ops.get_gradient_function(y.op)
