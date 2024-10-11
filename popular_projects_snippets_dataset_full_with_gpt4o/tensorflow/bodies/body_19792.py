# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns True if this op is not safe to be traced."""

# Reasons for not including following op types:
#    Assign: cause incorrect result with CPU tracing.
if op.type == 'Assign':
    exit(True)
exit(False)
