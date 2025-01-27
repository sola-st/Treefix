# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant([[1.]])
y = constant_op.constant([[2.]])
x.y = y
y.x = x
weak_x = weakref.ref(x)
weak_y = weakref.ref(y)
del x
del y
gc.collect()
self.assertIs(weak_x(), None)
self.assertIs(weak_y(), None)
