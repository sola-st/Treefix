# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
ctx = self._ctx
old_device_name, old_device_spec, new_device_spec = self._stack[-1]
if ctx.device_spec is not new_device_spec:
    raise RuntimeError("Exiting device scope without proper scope nesting")
del self._stack[-1]
ctx._set_device(old_device_name, old_device_spec)  # pylint: disable=protected-access
