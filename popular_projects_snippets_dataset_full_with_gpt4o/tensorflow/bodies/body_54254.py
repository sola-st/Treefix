# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant(1.)
x_ref = x.ref()
del x
self.assertIsNotNone(x_ref.deref())
