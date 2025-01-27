# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = array_ops.constant(1)
self.assertEqual(f"{t}", "1")
self.assertEqual(str(t), "tf.Tensor(1, shape=(), dtype=int32)")
self.assertEqual(f"{t!s}", "tf.Tensor(1, shape=(), dtype=int32)")
self.assertEqual(repr(t), "<tf.Tensor: shape=(), dtype=int32, numpy=1>")
self.assertEqual(f"{t!r}", "<tf.Tensor: shape=(), dtype=int32, numpy=1>")
