# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
exit(self._parameters.trace_mode in (
    tensor_tracer_flags.TRACE_MODE_SUMMARY,
    tensor_tracer_flags.TRACE_MODE_FULL_TENSOR_SUMMARY))
