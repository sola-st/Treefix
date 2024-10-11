# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
with self.assertRaisesRegex(
    TypeError, "Expected string, but got 3 of type 'int'"
    "|Cannot convert 3 to EagerTensor of dtype string"):
    converter.Convert(3, types_pb2.DT_STRING)
