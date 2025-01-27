# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
with self.assertRaises((TypeError, ValueError)):
    converter.Convert(
        constant_op.constant([1, 2, 3], dtypes.int32), types_pb2.DT_INT64)
