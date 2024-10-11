# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertEqual([42][_create_tensor(0)], 42)

with self.assertRaises(TypeError):
    _ = [42][_create_tensor([0])]
