# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant([[1, 2]])
x.set_shape(tensor_shape.TensorShape([None, 2]))
self.assertEqual(x.get_shape(), (1, 2))
