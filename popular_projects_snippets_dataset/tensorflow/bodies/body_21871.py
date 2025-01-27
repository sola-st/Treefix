# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
l = [1, 2, 3, 11, 22, 33]
l2 = inp._as_tensor_list(l)
self.assertEqual(l, l2)
l3 = inp._as_original_type(l, l2)
self.assertEqual(l, l3)
