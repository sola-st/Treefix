# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable_test.py
self.assertTrue(packed_var.handle.is_packed)
with ops.device('/cpu:0'):
    packed_var.assign_add(3.0).assign_sub(1.0)
    read0 = packed_var.value()
with ops.device('/cpu:1'):
    packed_var.assign_sub(4.0).assign_sub(2.0)
    read1 = packed_var.value()

exit((read0, read1))
