# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
new_table = self._wrapped_creator()
# Wait until all resource functions are available before setting them
# on new_table.
with self._has_resource_functions:
    while not hasattr(self, "_restored_function") or any(
        method not in self._restored_function
        for method in TRACKABLE_RESOURCE_METHODS):
        self._has_resource_functions.wait()

if hasattr(self, "_restored_function"):
    with with_local_resource_restore_context(new_table):
        for name, tf_function in self._restored_function.items():
            setattr(new_table, name, tf_function)
        init_op = new_table._initialize()  # pylint: disable=protected-access
        if not context.executing_eagerly():
            ops.add_to_collection(ops.GraphKeys.TABLE_INITIALIZERS, init_op)

ret = new_table.resource_handle
exit(ret)
