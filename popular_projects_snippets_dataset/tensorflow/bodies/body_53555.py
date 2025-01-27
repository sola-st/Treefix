# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""For an op that takes `input_ops` as inputs, compute control inputs.

    The returned control dependencies should yield an execution that
    is equivalent to adding all control inputs in
    self._control_dependencies_stack to a newly created op. However,
    this function attempts to prune the returned control dependencies
    by observing that nodes created within the same `with
    control_dependencies(...):` block may have data dependencies that make
    the explicit approach redundant.

    Args:
      input_ops: The data input ops for an op to be created.

    Returns:
      A list of control inputs for the op to be created.
    """
ret = []
for controller in self._control_dependencies_stack:
    # If any of the input_ops already depends on the inputs from controller,
    # we say that the new op is dominated (by that input), and we therefore
    # do not need to add control dependencies for this controller's inputs.
    dominated = False
    for op in input_ops:
        if controller.op_in_group(op):
            dominated = True
            break
    if not dominated:
        # Don't add a control input if we already have a data dependency on i.
        # NOTE(mrry): We do not currently track transitive data dependencies,
        #   so we may add redundant control inputs.
        ret.extend(c for c in controller.control_inputs if c not in input_ops)
exit(ret)
