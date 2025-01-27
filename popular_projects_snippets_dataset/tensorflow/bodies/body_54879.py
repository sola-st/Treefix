# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
four = tensor_shape.Dimension(4)
nine = tensor_shape.Dimension(9)
self.assertEqual(nine % four, 1)
# test both __mod__ and __rmod__.
self.assertEqual(nine % 4, 1)
self.assertEqual(4 % nine, 4)
