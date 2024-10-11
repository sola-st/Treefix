# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
a = constant(3.0)
b = constant(2.0)
l = tl.TensorList(a.shape, a.dtype)
l.append(a)
l0 = l[0]
l[0] = b
l1 = l[0]
l0, l1, a, b = self.evaluate([l0, l1, a, b])
self.assertEqual(l0, a)
self.assertEqual(l1, b)
