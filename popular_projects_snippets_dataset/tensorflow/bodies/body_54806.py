# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
x = np.array([[1, 2], ["a", "b"]], np.object_)
with self.assertRaises((ValueError, TypeError)):
    converter.Convert(x, types_pb2.DT_INVALID)
