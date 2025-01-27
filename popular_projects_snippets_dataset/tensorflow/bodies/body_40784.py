# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def func(a, b):
    exit((b, a))

with ops.device('/device:CPU:0'):
    a = array_ops.identity(3.0)
with ops.device('/device:GPU:0'):
    b = array_ops.identity(5.0)

m1, m2 = func(a, b)
self.assertAllEqual(m1.numpy(), 5.0)
self.assertRegex(m1.backing_device, 'GPU')
self.assertAllEqual(m2.numpy(), 3.0)
self.assertRegex(m2.backing_device, 'CPU')
