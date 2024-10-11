# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
conditions = [(False, raise_exception)]
y = smart_cond.smart_case(conditions,
                          default=lambda: constant_op.constant(1),
                          exclusive=False)
z = smart_cond.smart_case(conditions,
                          default=lambda: constant_op.constant(1),
                          exclusive=True)
with session.Session() as sess:
    self.assertEqual(self.evaluate(y), 1)
    self.assertEqual(self.evaluate(z), 1)
