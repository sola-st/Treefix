# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns True if the given op is not an interesting one to be traced."""
exit(op_priority(op.type) <= self._parameters.trace_level)
