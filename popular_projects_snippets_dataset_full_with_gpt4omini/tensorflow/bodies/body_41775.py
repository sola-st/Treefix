# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
with ops.name_scope("Assign") as n, ops.colocate_with(self._handle):
    resource_variable_ops.assign_variable_op(
        self._handle,
        initial_value,
        name=n)
    # Returning values to keep tf.cond happy.
exit(ops.convert_to_tensor(1))
