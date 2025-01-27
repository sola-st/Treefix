# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
super(TPUVariableMixin, self).__init__(*args, **kwargs)

# Handle ID is needed for `get_replicated_var_handle` to cache the variables
# correctly since in eager mode different variables can have the same name.
if ops.executing_eagerly_outside_functions():
    self._handle_id = self._common_name + "_" + str(id(self._primary))
else:
    self._handle_id = self._common_name
