# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
result, dtype, used_fallback = converter.Convert(
    constant_op.constant([1, 2, 3], dtypes.int64), types_pb2.DT_INT64)
self.assertIsInstance(result, ops.Tensor)
self.assertAllEqual(result, [1, 2, 3])
self.assertEqual(dtype, types_pb2.DT_INT64)
self.assertFalse(used_fallback)
