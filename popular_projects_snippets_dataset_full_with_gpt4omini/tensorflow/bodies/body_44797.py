# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensor_list_test.py
with context.eager_mode():
    a = constant(3.0)
    b = constant(2.0)
    l = tl.TensorList(a.shape, a.dtype)
    l.append(a)
    self.assertEqual(l[0].numpy(), a.numpy())
    l[0] = ops.convert_to_tensor(b)
    self.assertEqual(l[0].numpy(), b.numpy())
