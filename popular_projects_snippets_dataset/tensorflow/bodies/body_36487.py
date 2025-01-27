# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape() as t:
    x = constant_op.constant(2.)
    t.watch(x)
    ret = while_loop_v2(
        lambda v: v < 4., lambda v: v * v, [x],
        return_same_structure=False)  # x**2
grad = t.gradient(ret, x)
with self.cached_session() as sess:
    self.assertAllEqual(sess.run(grad), 4.0)
