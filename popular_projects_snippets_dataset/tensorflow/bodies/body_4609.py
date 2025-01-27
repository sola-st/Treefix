# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
self.assertTrue(packed_var.handle.is_packed)
var0 = packed_distributed_variable.PackedVarAndDevice(packed_var, device0)
var0.assign_add(3.0)
var1 = packed_distributed_variable.PackedVarAndDevice(packed_var, device1)
exit((var0.value(), math_ops.add(var1, 2.0)))
