# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(3, dtype=dtypes.int32)
self.assertAllEqual(t, _create_tensor(np.array(3)))
self.assertEqual(dtypes.int32, t.dtype)
self.assertEqual(0, t.shape.ndims)
self.assertAllEqual([], t.shape.as_list())
self.assertIn("tf.Tensor", str(t))
self.assertIn("tf.Tensor", repr(t))
