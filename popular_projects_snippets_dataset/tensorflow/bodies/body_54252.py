# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x1 = constant_op.constant(3)
x2 = x1
y = constant_op.constant(3)
z = constant_op.constant([6, 10])
w = variables.Variable(5)

self.assertEqual(x1.ref(), x2.ref())

tensor_set = {
    x1.ref(),
    x2.ref(),
    y.ref(),
    z.ref(),
    w.ref(),
}

self.assertLen(tensor_set, 4)
self.assertIn(x1.ref(), tensor_set)
self.assertIn(x2.ref(), tensor_set)
self.assertIn(y.ref(), tensor_set)
self.assertIn(z.ref(), tensor_set)
self.assertIn(w.ref(), tensor_set)
