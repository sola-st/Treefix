# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
b = constant_op.constant([True, False], name="b")
x = constant_op.constant([13, 37], name="x")

self.assertAllInSet(b, [False, True])
self.assertAllInSet(b, (False, True))
self.assertAllInSet(b, {False, True})
self.assertAllInSet(x, [0, 13, 37, 42])
self.assertAllInSet(x, (0, 13, 37, 42))
self.assertAllInSet(x, {0, 13, 37, 42})

with self.assertRaises(AssertionError):
    self.assertAllInSet(b, [False])
with self.assertRaises(AssertionError):
    self.assertAllInSet(x, (42,))
