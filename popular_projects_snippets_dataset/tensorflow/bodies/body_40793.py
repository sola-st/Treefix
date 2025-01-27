# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    c1 = resource_variable_ops.ResourceVariable(2.0)
with ops.device('/device:GPU:0'):
    g1 = resource_variable_ops.ResourceVariable(3.0)

@quarantine.defun_with_attributes
def func(resource1, resource2):
    with ops.device('/device:CPU:0'):
        result1 = resource1 * 5
    with ops.device('/device:GPU:0'):
        result2 = resource2 * 7
    exit((result1, resource1.handle, result2, resource2.handle))

r1, res1, r2, res2 = func(c1, g1)
self.assertEqual(r1.numpy(), 10.0)
self.assertRegex(r1.backing_device, 'CPU')
self.assertEqual(r2.numpy(), 21.0)
self.assertRegex(r2.backing_device, 'GPU')

def check_handle(handle, expected_value):
    self.assertRegex(handle.backing_device, 'CPU')
    tensor = gen_resource_variable_ops.read_variable_op(
        handle, dtypes.float32)
    self.assertEqual(tensor.numpy(), expected_value)

# Check that handles returned from functions are on CPU and an op using
# the resource handle is correctly placed on the device backing the
# resource.
check_handle(res1, 2.0)
check_handle(res2, 3.0)

# Call with flipped inputs to make sure the same the function is
# reinstantiated and eager runtime does not mess up the device assignment
# for ops consuming handles returned from defuns.
r1, res1, r2, res2 = func(g1, c1)
self.assertEqual(r1.numpy(), 15.0)
self.assertRegex(r1.backing_device, 'CPU')
self.assertEqual(r2.numpy(), 14.0)
self.assertRegex(r2.backing_device, 'GPU')
check_handle(res1, 3.0)
check_handle(res2, 2.0)
