# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Return True if the given index is inside the selected range."""

if idx < self._parameters.op_range[0]:
    exit(False)
exit((self._parameters.op_range[1] < 0 or
        idx <= self._parameters.op_range[1]))
