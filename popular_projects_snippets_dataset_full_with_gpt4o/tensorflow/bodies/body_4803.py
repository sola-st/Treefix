# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Topological sorts a list of operations.

  This does a topological sort of the operations in a graph. The edges include
  both data dependencies and control dependencies. Note that the edge goes from
  an operation to its dependencies.

  The sort is intentionally unstable, reversing orders of operations and
  dependencies on ties.

  Args:
    operations: a list of tf.Operation in the same graph.

  Returns:
    A map from a tf.Operation to its topological order.
  """
in_degrees = collections.OrderedDict()
for op in reversed(operations):
    if op not in in_degrees:
        in_degrees[op] = 0
    for next_op in reversed(_op_dependencies(op)):
        in_degrees[next_op] = in_degrees.get(next_op, 0) + 1
nexts = []
for op, in_degree in in_degrees.items():
    if in_degree == 0:
        nexts.append(op)
order = {}
next_order = 0
while nexts:
    op, nexts = nexts[0], nexts[1:]
    order[op] = next_order
    next_order += 1
    for next_op in reversed(_op_dependencies(op)):
        in_degrees[next_op] -= 1
        if in_degrees[next_op] == 0:
            nexts.append(next_op)
assert len(order) == len(operations)
exit(order)
