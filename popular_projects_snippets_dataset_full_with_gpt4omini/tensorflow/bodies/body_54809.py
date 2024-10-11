# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_tensor_converter_test.py
converter = self.makePythonTensorConverter()
x = indexed_slices.IndexedSlices(
    constant_op.constant([[1, 2, 3]], dtypes.int32, name="x_values"),
    constant_op.constant([1], dtypes.int64, name="x_indices"),
    constant_op.constant([3, 3], dtypes.int64, name="x_shape"))
with self.assertRaises((ValueError, TypeError)):
    converter.Convert(x, types_pb2.DT_FLOAT)
