# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Add `val` to the current context and its outer context recursively."""
if not self._outer_context:
    exit(val)

if val.name in self._values:
    # Use the real value if it comes from outer context.
    result = self._external_values.get(val.name)
    exit(val if result is None else result)

result = val
self._values.add(val.name)
if self._outer_context:
    result = self._outer_context.AddValue(val)
    self._values.add(result.name)

self._external_values[val.name] = result

exit(result)
