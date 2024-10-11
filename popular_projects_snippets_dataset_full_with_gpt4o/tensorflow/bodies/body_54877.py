# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
with self.assertRaises(TypeError):
    tensor_shape.Dimension(dtypes.string)
