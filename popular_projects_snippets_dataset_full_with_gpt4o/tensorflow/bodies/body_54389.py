# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = test_ops.float_output()
y = test_ops.copy_op(x)
fn = ops.get_gradient_function(y.op)
self.assertEqual(_CopyGrad, fn)
