# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = constant_op.constant(2)
y = constant_op.constant(1)
z = control_flow_ops.cond(
    math_ops.less(x, y),
    fn1=lambda: math_ops.multiply(x, 17),
    fn2=lambda: math_ops.add(y, 23))
self.assertEqual(self.evaluate(z), 24)
