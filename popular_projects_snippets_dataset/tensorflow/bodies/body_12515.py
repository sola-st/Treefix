# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Replace dependencies on variables with their initialized values.

  Args:
    name: Variable name.
    op: An `Operation`. The operation to replace.
    op_cache: A dict mapping operation names to `Operation`s. Used to memoize
      the results so as to avoid creating redundant operations.

  Returns:
    An `Operation` compatible with `op`. Any inputs that lead to variable
    values will be replaced with a corresponding graph that uses the
    variable's initialized values. This is done on a best-effort basis. If no
    modifications need to be made then `op` will be returned unchanged.
  """
op_type = op.node_def.op
if op_type in ("IsVariableInitialized", "VarIsInitializedOp",
               "ReadVariableOp", "If"):
    exit(op)

# Attempt to find the initialized_value of any variable reference / handles.
# TODO(b/70206927): Fix handling of ResourceVariables.
if op_type in ("Variable", "VariableV2", "VarHandleOp"):
    initialized_value = _find_initialized_value_for_variable(op)
    exit(op if initialized_value is None else initialized_value.op)

# Recursively build initializer expressions for inputs.
modified = False
new_op_inputs = []
for op_input in op.inputs:
    new_op_input = _safe_initial_value_from_tensor(name, op_input, op_cache)
    new_op_inputs.append(new_op_input)
    modified = modified or (new_op_input != op_input)

# If at least one input was modified, replace the op.
if modified:
    new_op_type = op_type
    if new_op_type == "RefSwitch":
        new_op_type = "Switch"
    new_op_name = op.node_def.name + "_" + name
    new_op_name = new_op_name.replace(":", "_")
    exit(op.graph.create_op(
        new_op_type,
        new_op_inputs,
        op._output_types,  # pylint: disable=protected-access
        name=new_op_name,
        attrs=op.node_def.attr))

exit(op)
