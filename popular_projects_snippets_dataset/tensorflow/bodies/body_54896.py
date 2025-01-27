# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
unknown = tensor_shape.Dimension(None)
self.assertEqual((unknown // unknown).value, None)
with self.assertRaisesRegex(TypeError, r"unsupported operand type"):
    unknown / unknown  # pylint: disable=pointless-statement
