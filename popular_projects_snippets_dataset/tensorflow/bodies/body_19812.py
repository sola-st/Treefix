# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns true if the whole tensor needs to be cached/buffered in memory."""
exit((self._parameters.trace_mode ==
        tensor_tracer_flags.TRACE_MODE_FULL_TENSOR_SUMMARY))
