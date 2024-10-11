# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Wraps the trace_fn with outside compilation if on TPUs."""
tensor_trace_fn = self._make_tensor_trace_fun(out_tensor_name,
                                              tensor_trace_order)
if on_tpu:
    exit(tpu.outside_compilation(tensor_trace_fn, tensor))
else:
    exit(tensor_trace_fn(tensor))
