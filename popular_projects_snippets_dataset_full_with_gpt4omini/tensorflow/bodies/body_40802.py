# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Tests input/output mapping logic in partitioning."""
with ops.device('/device:CPU:0'):
    rc0 = resource_variable_ops.ResourceVariable(2.0)
    rc1 = resource_variable_ops.ResourceVariable(3.0)
    cc0 = array_ops.identity(5.0)
    cc1 = array_ops.identity(7.0)
with ops.device('/device:GPU:0'):
    rg0 = resource_variable_ops.ResourceVariable(11.0)
    rg1 = resource_variable_ops.ResourceVariable(13.0)
    cg0 = array_ops.identity(17.0)
    cg1 = array_ops.identity(19.0)

# Make sure tensors are on expected devices.
for tensor in [cc0, cc1]:
    self.assertRegex(tensor.backing_device, 'CPU:0')
for tensor in [cg0, cg1]:
    self.assertRegex(tensor.backing_device, 'GPU:0')

@quarantine.defun_with_attributes
def func(rc0, cc0, cg0, rc1, cg1, rg0, rg1, cc1):
    with ops.device('/device:CPU:0'):
        m1 = rc0 * cg0
    with ops.device('/device:GPU:0'):
        m2 = rg0 * cc0

    with ops.device('/device:CPU:0'):
        r1 = 1000.0 * m2 + rc1 * cg1
    with ops.device('/device:GPU:0'):
        r2 = 1000.0 * m1 + rg1 * cc1

    exit((r1, r2, m2, m1))

r1, r2, m2, m1 = func(rc0, cc0, cg0, rc1, cg1, rg0, rg1, cc1)
self.assertRegex(m1.backing_device, 'CPU')
self.assertRegex(r1.backing_device, 'CPU')
self.assertRegex(m2.backing_device, 'GPU')
self.assertRegex(r2.backing_device, 'GPU')
self.assertEqual(m1.numpy(), 34.0)
self.assertEqual(r1.numpy(), 55000.0 + 3.0 * 19.0)
self.assertEqual(m2.numpy(), 55.0)
self.assertEqual(r2.numpy(), 34000.0 + 13.0 * 7.0)
