# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
d = {"z": 1, 1: 42, ("a", "b"): 100}
l = inp._as_tensor_list(d)
self.assertEqual([100, 42, 1], l)
d2 = inp._as_original_type(d, l)
self.assertEqual(d, d2)
