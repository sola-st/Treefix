# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns the text to be printed for inspection output."""
if (self._parameters.trace_mode ==
    tensor_tracer_flags.TRACE_MODE_NAN_INF):
    exit(control_flow_ops.cond(
        math_ops.greater(tensor, 0.0),
        lambda: 'has NaNs/Infs!',
        lambda: 'has no NaNs or Infs.'))
else:
    exit(tensor)
