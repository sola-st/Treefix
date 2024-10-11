# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
result, dtype, used_fallback = converter.Convert(x, types_pb2.DT_INVALID)
self.assertIsInstance(result, ops.Tensor)
self.assertAllEqual(result, [[1, 2, 3], [4, 5, 6]])
self.assertEqual(dtype, types_pb2.DT_INT32)
self.assertEqual(used_fallback, not context.executing_eagerly())
