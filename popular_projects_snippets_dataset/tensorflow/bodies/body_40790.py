# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    c1 = resource_variable_ops.ResourceVariable(2.0)
    c2 = resource_variable_ops.ResourceVariable(7.0)
with ops.device('/device:GPU:0'):
    g1 = resource_variable_ops.ResourceVariable(3.0)
    g2 = resource_variable_ops.ResourceVariable(5.0)

@quarantine.defun_with_attributes
def func(resource1, resource2):
    with ops.device('/device:CPU:0'):
        result1 = resource1 * g2
    with ops.device('/device:GPU:0'):
        result2 = resource2 * c2
    exit((result1, result2))

r1, r2 = func(c1, g1)
self.assertEqual(r1.numpy(), 10.0)
self.assertRegex(r1.backing_device, 'CPU')
self.assertEqual(r2.numpy(), 21.0)
self.assertRegex(r2.backing_device, 'GPU')

# Call with flipped inputs. Check that we look at resource's
# device and reinstantiates the function when inputs' devices change.
r1, r2 = func(g1, c1)
self.assertEqual(r1.numpy(), 15.0)
self.assertRegex(r1.backing_device, 'CPU')
self.assertEqual(r2.numpy(), 14.0)
self.assertRegex(r2.backing_device, 'GPU')
