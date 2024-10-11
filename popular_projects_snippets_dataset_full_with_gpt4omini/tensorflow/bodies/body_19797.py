# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Initializes a TensorTracer.

    Sets the various member fields from the flags (if given) or the defaults.
    """
self._replica_id = None
self._tt_config = tensor_tracer_report.TensorTracerConfig()
self._parameters = None
self._host_call_fn = {}
# _cache_variables is a dict (key = graph, value = dicts
# (key = name, value = tensors))
self._cache_variables = {}
self._history_value_cache = {}

self._traced_op_names = set()
self._report_proto = None
# _temp_cache_var is a dict (key = graph, value = [])
self._temp_cache_var = {}
self._report_proto_path = ''
self._outmost_context = None
