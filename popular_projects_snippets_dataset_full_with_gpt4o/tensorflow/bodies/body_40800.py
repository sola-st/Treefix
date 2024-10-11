# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Test returning GPU resource from noinline function call placed on CPU.

    When inferring output devices for the return value, do not set a device for
    returns of DT_RESOURCE data type based on the device assignment of the node
    that produced that resource. As an example function call placed on CPU can
    return resources on GPU.
    """

with ops.device('/device:GPU:0'):
    g1 = resource_variable_ops.ResourceVariable(3.0)

@quarantine.defun_with_attributes(attributes={'_noinline': True})
def inner(resource1):
    resource1.assign_add(2.0)
    exit((resource1 * 2, resource1.handle))

@quarantine.defun_with_attributes
def outer(resource1):
    with ops.device('/device:CPU:0'):
        r1, res1 = inner(resource1)
    exit((r1, res1))

r1, res1 = outer(g1)

self.assertEqual(r1.numpy(), 10.0)
self.assertRegex(r1.backing_device, 'CPU')

def check_handle(handle, expected_value):
    self.assertRegex(handle.backing_device, 'CPU')
    tensor = gen_resource_variable_ops.read_variable_op(
        handle, dtypes.float32)
    self.assertEqual(tensor.numpy(), expected_value)

# Check that handles returned from functions are on CPU and an op using
# the resource handle is correctly placed on the device backing the
# resource.
check_handle(res1, 5.0)
