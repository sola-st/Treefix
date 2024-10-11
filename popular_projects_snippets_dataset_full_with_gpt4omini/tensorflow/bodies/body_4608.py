# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
with ops.device('/cpu:0'):
    v0 = resource_variable_ops.ResourceVariable(1.0, name='var0')
with ops.device('/cpu:1'):
    v1 = resource_variable_ops.ResourceVariable(2.0, name='var1')

packed_var = packed_distributed_variable.PackedDistributedVariable([v0, v1])
self.assertFalse(packed_var.handle.is_packed)
self.assertTrue(packed_var.is_initialized)

with ops.device('/cpu:0'):
    self.assertAllEqual(packed_var.get_var_on_current_device(), v0)
    val0 = packed_var.assign(2.0).assign_add(1.0)
    self.assertAllEqual(val0, 3.0)

with ops.device('/cpu:1'):
    self.assertAllEqual(packed_var.get_var_on_current_device(), v1)
    val0 = packed_var.assign(2.0).assign_add(1.0)
    self.assertAllEqual(val0, 3.0)

@def_function.function
def update_var():
    self.assertTrue(packed_var.handle.is_packed)
    with ops.device('/cpu:0'):
        packed_var.assign_add(3.0).assign_sub(1.0)
        read0 = packed_var.value()
    with ops.device('/cpu:1'):
        packed_var.assign_sub(4.0).assign_sub(2.0)
        read1 = packed_var.value()

    exit((read0, read1))

self.assertAllEqual(update_var(), (5.0, -3.0))
