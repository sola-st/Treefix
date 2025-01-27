# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Raises an error if we backprop through a loop var."""
# Find the nearest 'to_op' reachable from 'op' to provide a more helpful error
# message.
target_op = None
queue = collections.deque([op])
visited = set()
while queue:
    curr_op = queue.popleft()
    if curr_op in visited: continue
    visited.add(curr_op)
    if curr_op in from_ops:
        target_op = curr_op
        break
    queue.extend(t.op for t in _NonEagerInputs(curr_op, xs_set))
assert target_op
raise ValueError(
    "Cannot compute gradient inside while loop with respect to op "
    f"'{target_op.name}'. We do not support taking the gradient wrt or "
    "through the initial value of a loop variable. Gradients can be computed "
    "through loop invariants or wrt the input parameters to the loop body.")
