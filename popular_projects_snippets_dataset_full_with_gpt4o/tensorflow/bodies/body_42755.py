# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = list_ops.tensor_list_reserve(
    element_shape=[1], num_elements=1, element_dtype=dtypes.float32)
self.assertEqual(f"{t}", "<TensorList>")
self.assertEqual(str(t), "tf.Tensor(<TensorList>, shape=(), dtype=variant)")
self.assertEqual(f"{t!s}",
                 "tf.Tensor(<TensorList>, shape=(), dtype=variant)")
self.assertEqual(
    repr(t), "<tf.Tensor: shape=(), dtype=variant, value=<TensorList>>")
self.assertEqual(
    f"{t!r}", "<tf.Tensor: shape=(), dtype=variant, value=<TensorList>>")
