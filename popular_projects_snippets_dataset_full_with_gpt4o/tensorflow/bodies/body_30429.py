# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# Regression test for bug in slice. A low-level bug in Eigen was causing
# incorrect results for negative indices in multi-dimensional tensors.
# See b/114318298.
with backprop.GradientTape(persistent=True) as tape:
    x = constant_op.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 7]])
    tape.watch(x)
    loss1 = math_ops.reduce_sum(x[:-1, :-1] * 1.0)
    loss2 = math_ops.reduce_sum(x[:-1][:, :-1])

g1 = tape.gradient(loss1, x)
g2 = tape.gradient(loss2, x)
g1_val, g2_val = self.evaluate([g1, g2])
self.assertAllEqual(g1_val, g2_val)
