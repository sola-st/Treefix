# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
if use_keep_prob and case_name != "stateful_v1":
    self.skipTest("Only V1 `dropout` has the `keep_prob` argument.")
if use_keep_prob:
    fn = lambda x, y: dropout_fn(x, keep_prob=y)
else:
    fn = lambda x, y: dropout_fn(x, rate=y)
x_dim = 40
y_dim = 30
t = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
with self.assertRaises(ValueError):
    fn(t, -1.0)
with self.assertRaises(ValueError):
    fn(t, 1.1)
with self.assertRaises(ValueError):
    fn(t, [0.0, 1.0])
with self.assertRaises(ValueError):
    fn(t, array_ops.placeholder(dtypes.float64))
with self.assertRaises(ValueError):
    fn(t, array_ops.placeholder(dtypes.float32, shape=[2]))
