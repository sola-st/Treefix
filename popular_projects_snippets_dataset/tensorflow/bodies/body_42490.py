# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Returns the dict of entries.

  Each entry is of the form {op_name, {true|false, indices}}

  true: All values are unused.
  false: `indices` are the only unused indices.

  Note: ops for which all values are used are not printed.

  Args:
    attr_name: inputs or outputs.

  Returns:
    A dict from op_type to formatted entry in the dict.
  """
assert attr_name in ["inputs", "outputs"]
entries = {}
for op_type in ops._gradient_registry.list():  # pylint: disable=protected-access
    if op_type in _EXCLUDED_OPS:
        continue
    num_values = _get_num_inputs_outputs(op_type)[0 if attr_name ==
                                                  "inputs" else 1]
    gradient_fn = ops._gradient_registry.lookup(op_type)  # pylint: disable=protected-access
    if gradient_fn is None:
        # NotDifferentiable
        if num_values != -1:
            entries[op_type] = "{\"%s\"}," % op_type
        continue
    used_tensors = _live_tensors(gradient_fn, attr_name=attr_name)
    if used_tensors is _ALL:
        continue
    elif not used_tensors:
        entries[op_type] = "{\"%s\"}," % op_type
    else:
        all_tensors = set(range(num_values))
        unused_tensors = all_tensors - used_tensors
        if unused_tensors:
            unused_tensor_list = sorted(list(unused_tensors))
            entries[op_type] = "{\"%s\", %d, {%s}}," % (
                op_type, len(unused_tensor_list), ", ".join(
                    str(i) for i in unused_tensor_list))
exit(entries)
