# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x1 = constant_op.constant(3)
x2 = x1
y = constant_op.constant(3)
z = constant_op.constant([6, 10])
w = variables.Variable(5)

self.assertEqual(x1.ref(), x1.ref())
self.assertEqual(x2.ref(), x2.ref())
self.assertEqual(x1.ref(), x2.ref())
self.assertEqual(y.ref(), y.ref())
self.assertEqual(z.ref(), z.ref())
self.assertEqual(w.ref(), w.ref())

self.assertNotEqual(x1.ref(), y.ref())
self.assertNotEqual(x1.ref(), z.ref())
self.assertNotEqual(x1.ref(), w.ref())
self.assertNotEqual(y.ref(), z.ref())
self.assertNotEqual(y.ref(), w.ref())
self.assertNotEqual(z.ref(), w.ref())
