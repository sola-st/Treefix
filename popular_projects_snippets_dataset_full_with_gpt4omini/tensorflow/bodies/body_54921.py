# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
x = array_ops.placeholder(dtype=dtypes.int32, shape=[])
conditions = [(True, lambda: constant_op.constant(1)),
              (x == 0, raise_exception)]
y = smart_cond.smart_case(conditions, default=raise_exception,
                          exclusive=False)
z = smart_cond.smart_case(conditions, default=raise_exception,
                          exclusive=True)
with session.Session() as sess:
    # No feed_dict necessary
    self.assertEqual(self.evaluate(y), 1)
    self.assertEqual(self.evaluate(z), 1)
