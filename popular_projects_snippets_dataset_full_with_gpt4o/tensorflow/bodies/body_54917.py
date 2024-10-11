# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    with session.Session():
        x = constant_op.constant(1)
        y = constant_op.constant(2)
        # x * y > 0 can be evaluated at graph construction time, so the false
        # branch shouldn't be evaluated at all.
        z = smart_cond.smart_cond(x * y > 0, lambda: constant_op.constant(1),
                                  raise_exception)
        self.assertEqual(z.eval(feed_dict={x: 1}), 1)
