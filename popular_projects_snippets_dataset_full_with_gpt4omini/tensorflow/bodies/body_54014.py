# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x_init = np.array([[10.0, 15.0]] * 12)
x = constant_op.constant(x_init, name="x")
with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 5, 10)
