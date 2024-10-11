# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x1 = constant_op.constant(3)
x2 = x1
y = constant_op.constant(3)
z = constant_op.constant([6, 10])
w = variables.Variable(5)

self.assertEqual(x1.ref(), x2.ref())

tensor_dict = {
    x1.ref(): "x1",
    y.ref(): "y",
    z.ref(): "z",
    w.ref(): "w",
}

self.assertLen(tensor_dict, 4)

# Overwriting x1
tensor_dict[x2.ref()] = "x2"
self.assertLen(tensor_dict, 4)

self.assertEqual(tensor_dict[x1.ref()], "x2")
self.assertEqual(tensor_dict[x2.ref()], "x2")
self.assertEqual(tensor_dict[y.ref()], "y")
self.assertEqual(tensor_dict[z.ref()], "z")
self.assertEqual(tensor_dict[w.ref()], "w")
