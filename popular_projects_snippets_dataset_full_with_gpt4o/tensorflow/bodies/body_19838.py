# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Determines the tensors to trace and instruments the trace details.

    Args:
      graph_order: graph_order tuple containing graph (tf.graph), operations
        (list of operations), op_to_idx (op id mapping), (tensors) list of
        tensors, tensor_to_idx (tensor id mapping), contains_cycle (whether
        there is a cycle in the graph), topological_order_or_cycle (list of ops
        in topological order or list of ops creating a cycle).
      ops_in_exec_path: Set of ops in the execution path.
      tensor_trace_points: Collection of programatic tensor trace points.
      report_handler: An instance of tensor_tracer_report.TTReportHandle.
    Returns:
      List of tensors to be traced.
    """

traced_tensors = []
checkpoint_operations = set([tensor.op
                             for (tensor, _) in tensor_trace_points])
for op_id, op in enumerate(graph_order.operations):
    if checkpoint_operations and op not in checkpoint_operations:
        continue
    if self._skip_op(op_id, op, ops_in_exec_path, report_handler):
        continue
    for i in range(len(op.outputs)):
        out_tensor = op.outputs[i]
        if not self._skip_tensor(op_id, out_tensor, report_handler):
            traced_tensors.append(out_tensor)
exit(traced_tensors)
