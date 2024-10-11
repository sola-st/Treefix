# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Tests that function's outputs respect colocation constraints."""

@quarantine.defun_with_attributes
def func(a, b):
    with ops.colocate_with(a):
        ra = 2 * a
    with ops.colocate_with(b):
        rb = 3 * b
    exit((ra, rb))

devices = ['/device:CPU:0', '/device:GPU:0']
for dev1, dev2 in itertools.product(devices, devices):
    with ops.device(dev1):
        a = array_ops.identity(1.0)
    with ops.device(dev2):
        b = array_ops.identity(10.0)

    ra, rb = func(a, b)
    self.assertEqual(ra.numpy(), 2.0)
    self.assertRegex(ra.backing_device, dev1)
    self.assertEqual(rb.numpy(), 30.0)
    self.assertRegex(rb.backing_device, dev2)
