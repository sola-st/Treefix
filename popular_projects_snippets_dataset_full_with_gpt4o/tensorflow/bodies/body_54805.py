# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
with self.assertRaises((ValueError, TypeError)):
    converter.Convert(x, types_pb2.DT_STRING)
