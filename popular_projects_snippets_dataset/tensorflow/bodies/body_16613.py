# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Calculate a max_size for use by stack ops inside an XLA while_loop.

  Args:
    value: The value inside the while_loop forward context.  Used for printing
      error messages.
    while_ctxt: The forward context inside which value resides.  This does not
      always match the value's immediate context, as `value` may be inside e.g.
      a cond context inside the while_loop.

  Returns:
    A tensor containing the `max_size` to feed to a Stack initializer.

  Raises:
    ValueError: If `value` is nested inside a `while_loop` that either
      lacks a `maximum_iterations` parameter, or the `maximum_iterations`
      parameter:

        - is inside a `while_loop` that is a parent of the calling context, and
        - cannot be evaluated at graph build time to a constant.
  """
value_name = value.name
# curr_ctxt is the context that tf.gradients was called in.
curr_ctxt = ops.get_default_graph()._get_control_flow_context()  # pylint: disable=protected-access

curr_ctxt_name = curr_ctxt.name if curr_ctxt is not None else ""
max_size = constant_op.constant(1)

# Loop through all containing while contexts between value and the
# current context, multiplying together each context's
# max_iterations to get the maximum stack size.
while while_ctxt not in (None, curr_ctxt):
    max_iter = while_ctxt.maximum_iterations
    if max_iter is None:
        raise ValueError(
            "Cannot create a gradient accumulator for tensor '%s' inside "
            "XLA while_loop because maximum_iterations was not passed to "
            "the tf.while_loop call ('%s')." % (value_name, while_ctxt.name))

    # pylint: disable=protected-access
    max_iter_ctxt = max_iter.op._get_control_flow_context()
    # pylint: enable=protected-access

    # If max_iter_ctxt (non-strictly) contains curr_ctxt, then it's OK to use.
    if util.IsContainingContext(curr_ctxt, max_iter_ctxt):
        max_size *= max_iter
    else:
        # We cannot use max_iter because it's defined in a nested while
        # or cond context, so will fail if we try to use it as input to
        # any ops in curr_ctxt (e.g. max_size or the final accumulator
        # stack). Attempt to get a constant value out to use instead.
        const_max_iter = tensor_util.constant_value(max_iter)
        if const_max_iter is None:
            raise ValueError(
                "Cannot create a gradient accumulator for tensor '%s' inside XLA "
                "while_loop. maximum_iterations tensor '%s' for while_loop context "
                "'%s' must be statically known (e.g. a constant value or known "
                "shape dimension), or be defined at or outside the while loop "
                "context '%s' (currently defined in '%s')." %
                (value_name, max_iter.name, while_ctxt.name, curr_ctxt_name,
                 max_iter_ctxt.name))
        max_size *= const_max_iter

    # Find the next outer WhileContext (or stop if we reach the
    # tf.gradient's context).
    while_ctxt = util.GetContainingWhileContext(
        while_ctxt.outer_context, stop_ctxt=curr_ctxt)

exit(max_size)
