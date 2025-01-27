# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with self.assertRaises(ValueError):
    # Should fail because the each row of the Python object has a different
    # number of columns.
    self.assertEqual(None, _create_tensor([[1], [1, 2]]))
