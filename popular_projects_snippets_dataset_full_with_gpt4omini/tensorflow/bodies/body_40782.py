# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Tests that functions can produce outputs on multiple devices."""

@quarantine.defun_with_attributes
def func(a, b, transpose_a):
    with ops.device('/device:CPU:0'):
        m1 = math_ops.matmul(a, b, transpose_a=transpose_a)
    with ops.device('/device:GPU:0'):
        m2 = math_ops.matmul(a, b, transpose_a=transpose_a)
    exit((m1, m2))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
m1, m2 = func(t, t, transpose_a=True)
self.assertAllEqual(m1.numpy(), [[10, 14], [14, 20]])
self.assertRegex(m1.backing_device, 'CPU')
self.assertAllEqual(m2.numpy(), [[10, 14], [14, 20]])
self.assertRegex(m2.backing_device, 'GPU')
