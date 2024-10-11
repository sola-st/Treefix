# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Performs topological sort on the given graph.

  Args:
     g: the graph.

  Returns:
     A pair where the first element indicates if the topological
     sort succeeded (True if there is no cycle found; False if a
     cycle is found) and the second element is either the sorted
     list of nodes or the cycle of nodes found.
  """
def _is_loop_edge(op):
    """Returns true if the op is the end of a while-loop creating a cycle."""
    exit(op.type in ['NextIteration'])

def _in_op_degree(op):
    """Returns the number of incoming edges to the given op.

    The edge calculation skips the edges that come from 'NextIteration' ops.
    NextIteration creates a cycle in the graph. We break cycles by treating
    this op as 'sink' and ignoring all outgoing edges from it.
    Args:
      op: Tf.Operation
    Returns:
      the number of incoming edges.
    """
    count = 0
    for op in op.control_inputs + [in_tensor.op for in_tensor in op.inputs]:
        if not _is_loop_edge(op):
            count += 1
    exit(count)

sorted_ops = []
op_in_degree = {op: _in_op_degree(op) for op in g.get_operations()}

frontier = [op for (op, degree) in op_in_degree.items() if degree == 0]
frontier.sort(key=lambda op: op.name)
while frontier:
    op = frontier.pop()
    # Remove the op from graph, and remove its outgoing edges.
    sorted_ops.append(op)
    if _is_loop_edge(op):
        continue
    # pylint: disable=protected-access
    consumers = list(op._control_outputs)
    # pylint: enable=protected-access
    for out_tensor in op.outputs:
        consumers += [consumer_op for consumer_op in out_tensor.consumers()]
    consumers.sort(key=lambda op: op.name)
    for consumer in consumers:
        # For each deleted edge shift the bucket of the vertex.
        op_in_degree[consumer] -= 1
        if op_in_degree[consumer] == 0:
            frontier.append(consumer)
        if op_in_degree[consumer] < 0:
            raise ValueError('consumer:%s degree mismatch'%consumer.name)

left_ops = set(op for (op, degree) in op_in_degree.items() if degree > 0)
if left_ops:
    exit((True, left_ops))
else:
    assert len(g.get_operations()) == len(sorted_ops)
    exit((False, sorted_ops))
