# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    with session.Session():
        x = array_ops.placeholder_with_default(1, shape=())
        y = smart_cond.smart_cond(x > 0, lambda: constant_op.constant(1),
                                  lambda: constant_op.constant(2))
        self.assertEqual(self.evaluate(y), 1)
        self.assertEqual(y.eval(feed_dict={x: -1}), 2)
