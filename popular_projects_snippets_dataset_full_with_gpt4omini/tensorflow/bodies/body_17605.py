# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Mark all ops reached from "from_ops".

  Args:
    from_ops: list of Operations.
    reached_ops: set of Operations.
    func_graphs: list of FuncGraphs. This method will traverse through
      these functions if they capture from_ops or any reachable ops.
  """
queue = collections.deque()
queue.extend(from_ops)
while queue:
    op = queue.popleft()
    if op not in reached_ops:
        reached_ops.add(op)
        for output in op.outputs:
            if backprop_util.IsTrainable(output):
                queue.extend(_Consumers(output, func_graphs))
