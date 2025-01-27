# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
# Note: This test is related to GitHub issue 25790.
six = tensor_shape.Dimension(6)
two = tensor_shape.Dimension(2)
message = (r"unsupported operand type\(s\) for /: "
           r"'Dimension' and 'Dimension', please use // instead")
with self.assertRaisesRegex(TypeError, message):
    _ = six / two
message = (r"unsupported operand type\(s\) for /: "
           r"'Dimension' and 'int', please use // instead")
with self.assertRaisesRegex(TypeError, message):
    _ = six / 2
message = (r"unsupported operand type\(s\) for /: "
           r"'int' and 'Dimension', please use // instead")
with self.assertRaisesRegex(TypeError, message):
    _ = 6 / two
