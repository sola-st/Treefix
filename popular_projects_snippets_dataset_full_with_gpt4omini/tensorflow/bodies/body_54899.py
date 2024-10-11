# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual("<unknown>", str(tensor_shape.unknown_shape()))
self.assertEqual(
    "(None,)",
    str(tensor_shape.unknown_shape(rank=1)).replace("?", "None"))
self.assertEqual(
    "(None, None)",
    str(tensor_shape.unknown_shape(rank=2)).replace("?", "None"))
self.assertEqual(
    "(None, None, None)",
    str(tensor_shape.unknown_shape(rank=3)).replace("?", "None"))
self.assertEqual(
    "(32, None, 1, 9)",
    str(tensor_shape.TensorShape([32, None, 1, 9])).replace("?", "None"))
self.assertEqual("()", str(tensor_shape.TensorShape([])))
self.assertEqual("(7,)", str(tensor_shape.TensorShape([7])))
self.assertEqual("(3, 8)", str(tensor_shape.TensorShape([3, 8])))
self.assertEqual("(4, 5, 2)", str(tensor_shape.TensorShape([4, 5, 2])))
