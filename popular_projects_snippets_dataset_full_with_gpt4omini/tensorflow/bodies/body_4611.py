# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
device0 = device_util.canonicalize('/cpu:0')
device1 = device_util.canonicalize('/cpu:1')

with ops.device(device0):
    v0 = resource_variable_ops.ResourceVariable(1.0)
with ops.device(device1):
    v1 = resource_variable_ops.ResourceVariable(2.0)

packed_var = packed_distributed_variable.PackedDistributedVariable([v0, v1])
# This needs a workaround to avoid creating reference cycles if the
# attribute doesn't exist.
hasattr(packed_var.on_device('/cpu:0'), 'nonexist')
