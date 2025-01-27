# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a = 7
b = (2., 3.)
c = np.ones((3, 2, 4)) * 7.
d = "testing123"
expected = {"a": a, "b": b, "c": c, "d": d}
actual = {"a": a, "b": b, "c": constant_op.constant(c), "d": d}

self.assertDictEqual(expected, expected)
self.assertDictEqual(expected, actual)
