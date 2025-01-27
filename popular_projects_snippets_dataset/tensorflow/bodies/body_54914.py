# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    with session.Session():
        x = constant_op.constant(2)
        y = constant_op.constant(5)
        z = smart_cond.smart_cond(True, lambda: math_ops.multiply(x, 16),
                                  lambda: math_ops.multiply(y, 5))
        self.assertEqual(self.evaluate(z), 32)
