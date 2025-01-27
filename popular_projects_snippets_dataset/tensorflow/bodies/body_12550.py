# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Adds ops to list the names of uninitialized variables.

  When run, it returns a 1-D tensor containing the names of uninitialized
  variables if there are any, or an empty array if there are none.

  Args:
    var_list: List of `Variable` objects to check. Defaults to the value of
      `global_variables() + local_variables()`
    name: Optional name of the `Operation`.

  Returns:
    A 1-D tensor containing names of the uninitialized variables, or an empty
    1-D tensor if there are no variables or no uninitialized variables.
  """
if var_list is None:
    var_list = global_variables() + local_variables()
    # Backwards compatibility for old-style variables. TODO(touts): remove.
    if not var_list:
        var_list = []
        for op in ops.get_default_graph().get_operations():
            if op.type in ["Variable", "VariableV2", "AutoReloadVariable"]:
                var_list.append(op.outputs[0])
with ops.name_scope(name):
    # Run all operations on CPU
    if var_list:
        init_vars = [state_ops.is_variable_initialized(v) for v in var_list]
    local_device = os.environ.get(
        "TF_DEVICE_FOR_UNINITIALIZED_VARIABLE_REPORTING", "/cpu:0")
    with ops.device(local_device):
        if not var_list:
            # Return an empty tensor so we only need to check for returned tensor
            # size being 0 as an indication of model ready.
            exit(array_ops.constant([], dtype=dtypes.string))
        else:
            # Get a 1-D boolean tensor listing whether each variable is initialized.
            variables_mask = math_ops.logical_not(array_ops.stack(init_vars))
            # Get a 1-D string tensor containing all the variable names.
            variable_names_tensor = array_ops.constant(
                [s.op.name for s in var_list])
            # Return a 1-D tensor containing all the names of
            # uninitialized variables.
            exit(array_ops.boolean_mask(variable_names_tensor, variables_mask))
