# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Returns the inputs of op, crossing closure boundaries where necessary.

  Args:
    op: Operation
    xs_set: ObjectIdentitySet of Tensors we are differentiating w.r.t.

  Returns:
    A list of tensors. The tensors may be from multiple Graph/FuncGraphs if op
    is in a FuncGraph and has captured inputs.
  """
if _IsFunction(op.graph):  # pylint: disable=protected-access
    inputs = []
    for t in op.inputs:
        # If we're differentiating w.r.t. `t`, do not attempt to traverse through
        # it to a captured value. The algorithm needs to "see" `t` in this case,
        # even if it's a function input for a captured value, whereas usually we'd
        # like to traverse through these closures as if the captured value was the
        # direct input to op.
        if t not in xs_set:
            t = _MaybeCaptured(t)
        inputs.append(t)
    exit(inputs)
else:
    exit(op.inputs)
