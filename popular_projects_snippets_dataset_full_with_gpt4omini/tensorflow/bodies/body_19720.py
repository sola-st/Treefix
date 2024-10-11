# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
if self.trace_mode in (TRACE_MODE_SUMMARY, TRACE_MODE_FULL_TENSOR_SUMMARY):
    if not self.trace_dir:
        raise ValueError('trace_dir must be explicitly provided in '
                         'TENSOR_TRACER_FLAGS when summary mode is used.')
