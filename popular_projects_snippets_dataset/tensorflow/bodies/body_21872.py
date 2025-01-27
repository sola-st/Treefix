# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
d = {"a": 1, "b": 2, "c": 3, "aa": 11, "bb": 22, "cc": 33}
l = inp._as_tensor_list(d)
self.assertEqual([1, 11, 2, 22, 3, 33], l)
d2 = inp._as_original_type(d, l)
self.assertEqual(d, d2)
