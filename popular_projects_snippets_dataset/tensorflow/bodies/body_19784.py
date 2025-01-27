# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Programmatic interface to trace a tensor with Tensor Tracer.

  Tensor Tracer, by default, traces all tensors in the execution. This function
  can be used to limit traced tensors. If this function is called for a subset
  of the tensors, only those will be traced.

  For example, Tensor Traacer will only trace c below.
    c = tf.MatMul(a, b)
    tensor_tracer.trace_tensor(c)
    d = tf.add(c, 1)
  Args:
     tensor: the tensor object for which the tracing is requested.
     tracepoint_name: an optional tensor tracepoint name string. A tracepoint
       name is an Tensor Tracer internal name for the tensor. It is useful when
       comparing equivalent traces from different models that have different
       tensor namings. Equivalent tensors (with different names) can be mapped
       to each other by assigning a common tracepoint_name.

  Returns:
    The provided tensor.
  """
if tracepoint_name is None:
    tracepoint_name = tensor.name
tensor.graph.get_collection(_TENSOR_TRACER_COLLECTION)
tensor.graph.add_to_collection(_TENSOR_TRACER_COLLECTION,
                               (tensor, tracepoint_name))
exit(tensor)
