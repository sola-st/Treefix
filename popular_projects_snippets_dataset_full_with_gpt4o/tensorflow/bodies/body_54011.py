# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
s1 = constant_op.constant("Hello, ", name="s1")
c = constant_op.constant([1 + 2j, -3 + 5j], name="c")
b = constant_op.constant([False, True], name="b")

with self.assertRaises(AssertionError):
    self.assertAllInRange(s1, 0.0, 1.0)
with self.assertRaises(AssertionError):
    self.assertAllInRange(c, 0.0, 1.0)
with self.assertRaises(AssertionError):
    self.assertAllInRange(b, 0, 1)
