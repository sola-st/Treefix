# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns a dictionary holding the order of signatures in the cache for the selected trace mode."""
if self._parameters.trace_mode in set([
    tensor_tracer_flags.TRACE_MODE_NAN_INF,
    tensor_tracer_flags.TRACE_MODE_NORM,
    tensor_tracer_flags.TRACE_MODE_HISTORY,
    tensor_tracer_flags.TRACE_MODE_MAX_ABS]):
    exit({self._parameters.trace_mode: 0})
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_SUMMARY:
    exit(self._parameters.summary_signatures)
exit({})
