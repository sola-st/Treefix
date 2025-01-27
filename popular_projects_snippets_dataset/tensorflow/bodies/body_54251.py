# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x1 = constant_op.constant(3)
x2 = x1
y = constant_op.constant(3)
z = constant_op.constant([6, 10])
w = variables.Variable(5)

self.assertIs(x1, x1.ref().deref())
self.assertIs(x2, x2.ref().deref())
self.assertIs(x1, x2.ref().deref())
self.assertIs(x2, x1.ref().deref())
self.assertIs(y, y.ref().deref())
self.assertIs(z, z.ref().deref())

self.assertIsNot(x1, y.ref().deref())
self.assertIsNot(x1, z.ref().deref())
self.assertIsNot(x1, w.ref().deref())
self.assertIsNot(y, z.ref().deref())
self.assertIsNot(y, w.ref().deref())
self.assertIsNot(z, w.ref().deref())
