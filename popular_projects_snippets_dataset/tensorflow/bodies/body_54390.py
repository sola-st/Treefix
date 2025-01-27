# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.float_output()
    with g.gradient_override_map({"CopyOp": "copy_override"}):
        y = test_ops.copy_op(x)
    fn = ops.get_gradient_function(y.op)
    self.assertEqual(_CopyOverrideGrad, fn)
