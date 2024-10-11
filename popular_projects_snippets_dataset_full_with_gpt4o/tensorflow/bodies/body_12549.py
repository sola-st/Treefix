# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns an Op to check if variables are initialized.

  NOTE: This function is obsolete and will be removed in 6 months.  Please
  change your implementation to use `report_uninitialized_variables()`.

  When run, the returned Op will raise the exception `FailedPreconditionError`
  if any of the variables has not yet been initialized.

  Note: This function is implemented by trying to fetch the values of the
  variables. If one of the variables is not initialized a message may be
  logged by the C++ runtime. This is expected.

  Args:
    var_list: List of `Variable` objects to check. Defaults to the value of
      `global_variables().`

  Returns:
    An Op, or None if there are no variables.
  """
if var_list is None:
    var_list = global_variables() + local_variables()
# Backwards compatibility for old-style variables. TODO(touts): remove.
if not var_list:
    var_list = []
    for op in ops.get_default_graph().get_operations():
        if op.type in ["Variable", "VariableV2", "AutoReloadVariable"]:
            var_list.append(op.outputs[0])
if not var_list:
    exit(None)
else:
    ranks = []
    for var in var_list:
        with ops.colocate_with(var.op):
            ranks.append(array_ops.rank_internal(var, optimize=False))
    if len(ranks) == 1:
        exit(ranks[0])
    else:
        exit(array_ops.stack(ranks))
