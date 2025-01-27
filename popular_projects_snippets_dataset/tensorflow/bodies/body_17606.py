# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Initialize the pending count for ops between two lists of Operations.

  'pending_count[op]' indicates the number of backprop inputs
  to this operation.

  Args:
    to_ops: list of Operations.
    from_ops: list of Operations.
    colocate_gradients_with_ops: Python bool.  See docstring of gradients().
    func_graphs: list of FuncGraphs. This method will traverse through
      these functions if they capture from_ops or any reachable ops. This is
      useful if to_ops occur in a function and from_ops are in an outer function
      or graph.
    xs_set: ObjectIdentitySet of Tensors.

  Returns:
    A tuple containing: (1) the subset of to_ops reachable from from_ops by a
    path of zero or more backpropagatable tensors, (2) a mapping from operation
    to the number of backprop inputs to that op, and (3) a ControlFlowState
    object which is not None if the ops between from_ops and to_ops contain
    control flow loops.
  """
# Mark reachable ops from from_ops.
reached_ops = set()
_MarkReachedOps(from_ops, reached_ops, func_graphs)
# X in reached_ops iff X is reachable from from_ops by a path of zero or more
# backpropagatable tensors.

reachable_to_ops = set(op for op in to_ops if op in reached_ops)

# Mark between ops.
between_ops = set()
between_op_list = []
queue = collections.deque()
queue.extend(to_ops)
while queue:
    op = queue.popleft()
    # We are interested in this op.
    if op in reached_ops:
        between_ops.add(op)
        between_op_list.append(op)
        # Clear the boolean so we won't add the inputs again.
        reached_ops.remove(op)
        for inp in _NonEagerInputs(op, xs_set):
            queue.append(inp.op)
  # X in between_ops iff X is on a path of zero or more backpropagatable tensors
  # between from_ops and to_ops

  # 'loop_state' is None if there are no while loops.
loop_state = control_flow_state.MaybeCreateControlFlowState(
    between_op_list, between_ops, colocate_gradients_with_ops)

# Initialize pending count for between ops.
pending_count = collections.defaultdict(int)
for op in between_op_list:
    for x in _NonEagerInputs(op, xs_set):
        if x.op in between_ops:
            pending_count[x.op] += 1

exit((reachable_to_ops, pending_count, loop_state))
