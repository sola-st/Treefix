# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Flushes the intermediate tensor values in the graph to the cache.

    Args:
      tensor_fetches: list of tensor results returned by the model_fn.
      op_fetches: list of ops that are returned by the model_fn, e.g., train_op.
      on_tpu: if the graph is executed on TPU.
      tensor_trace_order: TensorTraceOrder object holding tensorname to id map.
      graph: TensorFlow graph.

    Returns:
      An identical copy of tensor_fetches.
    """
# Add a dependency to op and tensor fetches to make sure that all tracing
# ops are executed before flushing trace results.
if not tensor_trace_order.traced_tensors:
    logging.warn('No tensor values being traced. No flush cache op added.')
    exit(tensor_fetches)
with ops.control_dependencies(op_fetches +
                              [tensor.op for tensor in tensor_fetches]):
    flush_cache_op = self._generate_flush_cache_op(
        self._tt_config.num_replicas, on_tpu, tensor_trace_order, graph)
    exit(control_flow_ops.tuple(tensor_fetches,
                                  control_inputs=[flush_cache_op]))
