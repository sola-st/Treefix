# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant([[1.]])
x.at1 = constant_op.constant([[2.]])
x.at2 = 3.
weak_x = weakref.ref(x)
weak_xat1 = weakref.ref(x.at1)
del x
self.assertIs(weak_x(), None)
self.assertIs(weak_xat1(), None)
