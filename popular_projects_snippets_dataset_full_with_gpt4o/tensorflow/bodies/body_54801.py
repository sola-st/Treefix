# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
with self.assertRaisesRegex(
    TypeError, "Expected string, but got .* of type 'int'"
    "|Cannot convert .* to EagerTensor of dtype string"):
    converter.Convert([[1, 2, 3], [4, 5, 6]], types_pb2.DT_STRING)
