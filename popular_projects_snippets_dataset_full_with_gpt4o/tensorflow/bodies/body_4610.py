# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
device0 = device_util.canonicalize('/cpu:0')
device1 = device_util.canonicalize('/cpu:1')

with ops.device(device0):
    v0 = resource_variable_ops.ResourceVariable(1.0)
with ops.device(device1):
    v1 = resource_variable_ops.ResourceVariable(2.0)

packed_var = packed_distributed_variable.PackedDistributedVariable([v0, v1])

packed_var0 = packed_distributed_variable.PackedVarAndDevice(
    packed_var, device0)
self.assertFalse(packed_var0.handle.is_packed)
self.assertAllEqual(math_ops.mul(packed_var0, 2.0), 2.0)

packed_var1 = packed_distributed_variable.PackedVarAndDevice(
    packed_var, device1)
self.assertAllEqual(packed_var1.assign(3.0), 3.0)

@def_function.function
def func():
    self.assertTrue(packed_var.handle.is_packed)
    var0 = packed_distributed_variable.PackedVarAndDevice(packed_var, device0)
    var0.assign_add(3.0)
    var1 = packed_distributed_variable.PackedVarAndDevice(packed_var, device1)
    exit((var0.value(), math_ops.add(var1, 2.0)))

self.assertAllEqual(func(), (4.0, 5.0))
