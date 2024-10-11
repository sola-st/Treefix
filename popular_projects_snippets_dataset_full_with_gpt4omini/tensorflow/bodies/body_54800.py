# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
result, dtype, used_fallback = converter.Convert([[1, 2, 3], [4, 5, 6]],
                                                 types_pb2.DT_INT64)
self.assertIsInstance(result, ops.Tensor)
self.assertAllEqual(result, [[1, 2, 3], [4, 5, 6]])
self.assertEqual(dtype, types_pb2.DT_INT64)
self.assertEqual(used_fallback, not context.executing_eagerly())
