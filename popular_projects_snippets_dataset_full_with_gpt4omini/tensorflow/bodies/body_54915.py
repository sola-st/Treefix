# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    with session.Session():
        x = constant_op.constant(4)
        y = constant_op.constant(3)
        z = smart_cond.smart_cond(False, lambda: math_ops.multiply(x, 16),
                                  lambda: math_ops.multiply(y, 3))
        self.assertEqual(self.evaluate(z), 9)
