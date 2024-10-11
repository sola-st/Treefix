# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Test passing GPU resource to noinline function call placed on CPU.

    PartitionedCallOp must not enforce any particular device assignment for the
    resource output. Inner function marked as `_nospecialize`, so Grappler would
    not prune unused function output.
    """

with ops.device('/device:GPU:0'):
    g1 = resource_variable_ops.ResourceVariable(3.0)

@quarantine.defun_with_attributes(attributes={
    '_noinline': True,
    '_nospecialize': True
})
def inner(resource1):
    exit((resource1 * 2, resource1.handle))

@quarantine.defun_with_attributes
def outer(resource1):
    with ops.device('/device:CPU:0'):
        r1, _ = inner(resource1)
    exit(r1)

r1 = outer(g1)

self.assertEqual(r1.numpy(), 6.0)
self.assertRegex(r1.backing_device, 'CPU')
