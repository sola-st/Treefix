# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a = [1, 2]
b = [1, 2, 5]
with self.assertRaises(AssertionError):
    self.assertArrayNear(a, b, 0.001)
a = [1, 2]
b = [[1, 2], [3, 4]]
with self.assertRaises(TypeError):
    self.assertArrayNear(a, b, 0.001)
a = [1, 2]
b = [1, 2]
self.assertArrayNear(a, b, 0.001)
