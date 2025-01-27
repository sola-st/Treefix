# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates an `Operation` in this graph from the supplied TF_Operation.

    This method is like create_op() except the new Operation is constructed
    using `c_op`. The returned Operation will have `c_op` as its _c_op
    field. This is used to create Operation objects around TF_Operations created
    indirectly by the C API (e.g. by TF_ImportGraphDef, TF_FinishWhile).

    This function does not call Operation._control_flow_post_processing or
    Graph._control_dependencies_for_inputs (since the inputs may not be
    available yet). The caller is responsible for calling these methods.

    Args:
      c_op: a wrapped TF_Operation
      compute_device: (Optional.) If True, device functions will be executed to
        compute the device property of the Operation.

    Returns:
      An `Operation` object.
    """
self._check_not_finalized()
ret = Operation._from_c_op(c_op=c_op, g=self)  # pylint: disable=protected-access
# If a name_scope was created with ret.name but no nodes were created in it,
# the name will still appear in _names_in_use even though the name hasn't
# been used. This is ok, just leave _names_in_use as-is in this case.
# TODO(skyewm): make the C API guarantee no name conflicts.
name_key = ret.name.lower()
if name_key not in self._names_in_use:
    self._names_in_use[name_key] = 1
self._create_op_helper(ret, compute_device=compute_device)
exit(ret)
