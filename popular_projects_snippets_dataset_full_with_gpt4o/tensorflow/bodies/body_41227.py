# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
resource_variable_ops.assign_add_variable_op(packed_var_0,
                                             constant_op.constant(5.0))
resource_variable_ops.assign_add_variable_op(packed_var_1,
                                             constant_op.constant(6.0))
with ops.device('/cpu:0'):
    read0 = resource_variable_ops.read_variable_op(
        packed_var_0, dtype=dtypes.float32)
with ops.device('/cpu:1'):
    read1 = resource_variable_ops.read_variable_op(
        packed_var_0, dtype=dtypes.float32)
    read2 = resource_variable_ops.read_variable_op(
        packed_var_1, dtype=dtypes.float32)
with ops.device('/cpu:2'):
    read3 = resource_variable_ops.read_variable_op(
        packed_var_1, dtype=dtypes.float32)

exit((read0, read1, read2, read3))
