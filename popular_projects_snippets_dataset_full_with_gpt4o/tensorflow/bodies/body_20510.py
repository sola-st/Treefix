# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
result = val
if self._outer_context:
    result = self._outer_context.AddValue(val)
exit(result)
