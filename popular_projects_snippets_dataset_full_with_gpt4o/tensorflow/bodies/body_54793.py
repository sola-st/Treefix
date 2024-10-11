# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
result, dtype, used_fallback = converter.Convert(12, types_pb2.DT_INVALID)
self.assertIsInstance(result, ops.Tensor)
self.assertAllEqual(result, 12)
self.assertEqual(dtype, types_pb2.DT_INT32)
self.assertEqual(used_fallback, not context.executing_eagerly())
