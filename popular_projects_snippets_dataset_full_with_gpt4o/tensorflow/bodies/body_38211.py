# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
with self.session():
    x = array_ops.zeros([3])
    b = clip_ops.clip_by_norm(x, 1.)
    grad, = gradients_impl.gradients(b, x)
    self.assertAllEqual(grad, [1., 1., 1.])
