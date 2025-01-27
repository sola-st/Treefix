# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
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
