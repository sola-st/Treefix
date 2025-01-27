# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Returns whether `input_op` can be used from `op`s context.

  Conceptually, only inputs from op's while context or any ancestor while
  context (including outside of any context) are valid. In practice, there are
  many other edge cases as well.

  Args:
    op: Operation
    input_op: Operation

  Raises:
    ValueError: if input_op is from an invalid context.
  """
op_ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
input_ctxt = GetOutputContext(input_op)
valid = False

if not input_ctxt:
    # input_op isn't in a control flow context.
    valid = True
elif op_ctxt is input_ctxt:
    # input_op is in the same context as op.
    valid = True
else:
    while_ctxt = GetContainingWhileContext(op_ctxt)
    input_while_ctxt = GetContainingWhileContext(input_ctxt)

    if while_ctxt is None:
        if input_while_ctxt is None:
            # Neither op nor input_op is in a while loop, but one or both are in
            # conds. We allow this, although execution will fail if the branch
            # corresponding to input_op's cond context isn't taken.
            valid = True
        # Invalid if op isn't in a while loop and input_op is. Unless...
        if IsLoopEnter(op):
            # WhileContext._BuildLoop clears context for Enter nodes.
            valid = True
        if IsSwitch(op):
            # CondContext.AddValue clears context for Switch nodes.
            valid = True
    elif IsContainingContext(while_ctxt, input_while_ctxt):
        # input_op is in a while loop which contains op's while loop (or not in a
        # while loop at all).
        valid = True
    elif (while_ctxt.grad_state and
          IsContainingContext(while_ctxt.grad_state.forward_context,
                              input_while_ctxt)):
        # op is in a gradient context and input_op is in the associated forward
        # pass context or an ancestor thereof. This case is need to build while
        # loop gradients.
        # NOTE(skyewm): we theoretically also need this case for custom gradient
        # functions that close over tensors from ancestor contexts, but I haven't
        # verified this.
        valid = True
    elif (while_ctxt.grad_state and
          while_ctxt.grad_state.forward_context is
          input_while_ctxt._outer_context):  # pylint: disable=protected-access
        # op is in a gradient context and input_op is in a child of the associated
        # forward pass context. This case is needed for the gradients of while
        # loops with conds.
        valid = True
    elif (input_while_ctxt.grad_state and
          input_while_ctxt.grad_state.forward_context is while_ctxt):
        # input_op is in the gradient context of op's context. This case is needed
        # when the gradient of a while loop gradient is requested (this will
        # eventually fail unless there is a stop_gradient() or similar).
        valid = True
    elif (input_while_ctxt.grad_state and
          input_ctxt.grad_state.forward_context.grad_state and
          input_ctxt.grad_state.forward_context.grad_state.forward_context is
          while_ctxt):
        # input_op is in the grad grad context of op's context. This case is
        # needed when the gradient of a while loop gradient is requested (this
        # will eventually fail unless there is a stop_gradient() or similar).
        valid = True

if not valid:
    if while_ctxt:
        error_msg = (
            f"Cannot use '{input_op.name}' as input to '{op.name}' because they "
            "are in different while loops.")
    else:
        error_msg = (
            f"Cannot use '{input_op.name}' as input to '{op.name}' because "
            f"'{input_op.name}' is in a while loop.")

    # Log the error message plus the relevant stack traces. The stacks may be
    # useful for debugging this error, but we don't want to raise an
    # unreadable exception.
    log_msg = error_msg
    log_msg += "\n\n%s while context: %s" % (op.name, while_ctxt)
    log_msg += "\n%s while context: %s" % (input_op.name, input_while_ctxt)
    log_msg += "\n\nTraceback for %s:\n%s\nTraceback for %s:\n%s\n" % (
        op.name, "".join(traceback.format_list(op.traceback)),
        input_op.name, "".join(traceback.format_list(input_op.traceback)))
    logging.info(log_msg)
    raise ValueError(error_msg + " See info log for more details.")
