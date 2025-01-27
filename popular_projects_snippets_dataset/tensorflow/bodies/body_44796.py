# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
with context.eager_mode():
    a = constant(3.0)
    l = tl.TensorList(a.shape, a.dtype)
    l.append(a)
    self.assertEqual(l.count().numpy(), 1)
    l.append(a)
    self.assertEqual(l.count().numpy(), 2)
    _ = l.pop()
    self.assertEqual(l.count().numpy(), 1)
    a2 = l.pop()
    self.assertEqual(l.count().numpy(), 0)
    self.assertEqual(a.numpy(), a2.numpy())
