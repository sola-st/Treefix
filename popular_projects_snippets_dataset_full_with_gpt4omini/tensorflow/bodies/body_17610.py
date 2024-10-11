# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""The set of ops that terminate the gradient computation.

  This computes the frontier of the forward graph *before* which backprop
  should stop. Operations in the returned set will not be differentiated.
  This set is defined as the subset of `from_ops` containing ops that have
  no predecessor in `from_ops`. `pending_count` is the result of
  `_PendingCount(xs, from_ops)`. An 'op' has predecessors in `from_ops`
  iff pending_count[op] > 0.

  In addition, none of `stop_gradient_ops` will be differentiated.

  Args:
    from_ops: list of Operations.
    stop_gradient_ops: list of Operations never to backprop through.
    pending_count: mapping from operation to number of backprop inputs.
    xs_set: ObjectIdentitySet of Tensors.

  Returns:
    The set of operations.
  """
stop_ops = set()
for op in from_ops:
    is_stop_op = True
    for inp in _NonEagerInputs(op, xs_set):
        if pending_count[inp.op] > 0:
            is_stop_op = False
            break
    if is_stop_op:
        stop_ops.add(op)
stop_ops.update(op for op in stop_gradient_ops)
exit(stop_ops)
