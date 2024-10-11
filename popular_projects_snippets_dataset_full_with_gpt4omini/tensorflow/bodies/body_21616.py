# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""See `init_from_checkpoint` for documentation."""
ckpt_file = _get_checkpoint_filename(ckpt_dir_or_file)
reader = load_checkpoint(ckpt_dir_or_file)
variable_map = reader.get_variable_to_shape_map()
if isinstance(assignment_map, abc.Mapping):
    assignment_map = assignment_map.items()

# We only want to sort by tensor names.
sort_key = lambda pair: pair[0]

for tensor_name_in_ckpt, current_var_or_name in sorted(
    assignment_map, key=sort_key):
    var = None
    # Check if this is Variable object or list of Variable objects (in case of
    # partitioned variables).
    if _is_variable(current_var_or_name) or (
        isinstance(current_var_or_name, list)
        and all(_is_variable(v) for v in current_var_or_name)):
        var = current_var_or_name
    else:
        store_vars = vs._get_default_variable_store()._vars  # pylint:disable=protected-access
        # Check if this variable is in var_store.
        var = store_vars.get(current_var_or_name, None)
        # Also check if variable is partitioned as list.
        if var is None:
            var = _collect_partitioned_variable(current_var_or_name, store_vars)
    if var is not None:
        # If 1 to 1 mapping was provided, find variable in the checkpoint.
        if tensor_name_in_ckpt not in variable_map:
            raise ValueError("Tensor %s is not found in %s checkpoint %s" % (
                tensor_name_in_ckpt, ckpt_dir_or_file, variable_map
            ))
        if _is_variable(var):
            # Additional at-call-time checks.
            if not var.get_shape().is_compatible_with(
                variable_map[tensor_name_in_ckpt]):
                raise ValueError(
                    "Shape of variable %s (%s) doesn't match with shape of "
                    "tensor %s (%s) from checkpoint reader." % (
                        var.name, str(var.get_shape()),
                        tensor_name_in_ckpt, str(variable_map[tensor_name_in_ckpt])
                    ))
            var_name = var.name
        else:
            var_name = ",".join(v.name for v in var)
        _set_variable_or_list_initializer(var, ckpt_file, tensor_name_in_ckpt)
        logging.debug("Initialize variable %s from checkpoint %s with %s",
                      var_name, ckpt_dir_or_file, tensor_name_in_ckpt)
    else:
        scopes = ""
        # TODO(vihanjain): Support list of 'current_var_or_name' here.
        if "/" in current_var_or_name:
            scopes = current_var_or_name[:current_var_or_name.rindex("/")]
        if not tensor_name_in_ckpt.endswith("/"):
            raise ValueError(
                "Assignment map with scope only name {} should map to scope only "
                "{}. Should be 'scope/': 'other_scope/'.".format(
                    scopes, tensor_name_in_ckpt))
        # If scope to scope mapping was provided, find all variables in the scope
        # and create variable to variable mapping.
        scope_variables = set()
        for var_name in store_vars:
            if not scopes or var_name.startswith(scopes + "/"):
                # Consume /part_ if partitioned variable.
                if "/part_" in var_name:
                    var_name = var_name[:var_name.index("/part_")]
                scope_variables.add(var_name)
        for var_name in sorted(scope_variables):
            # Lookup name with specified prefix and suffix from current variable.
            # If tensor_name given is '/' (root), don't use it for full name.
            full_tensor_name = var_name[len(scopes):]
            if current_var_or_name != "/":
                full_tensor_name = full_tensor_name[1:]
            if tensor_name_in_ckpt != "/":
                full_tensor_name = tensor_name_in_ckpt + full_tensor_name
            # Remove trailing '/', if any, in the full_tensor_name
            if full_tensor_name.endswith("/"):
                full_tensor_name = full_tensor_name[:-1]
            if full_tensor_name not in variable_map:
                raise ValueError(
                    "Tensor %s (%s in %s) is not found in %s checkpoint" % (
                        full_tensor_name, var_name[len(scopes) + 1:],
                        tensor_name_in_ckpt, ckpt_dir_or_file
                    ))
            var = store_vars.get(var_name, None)
            if var is None:
                var = _collect_partitioned_variable(var_name, store_vars)
            _set_variable_or_list_initializer(var, ckpt_file, full_tensor_name)
            logging.debug("Initialize variable %s from checkpoint %s with %s",
                          var_name, ckpt_dir_or_file, full_tensor_name)
