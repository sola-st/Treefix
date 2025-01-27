# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
with self.assertRaisesRegex(
    (TypeError, ValueError),
    "Can't convert Python sequence with mixed types to Tensor."
    "|Failed to convert"):
    converter.Convert([[1, 2], ["a", "b"]], types_pb2.DT_INVALID)
