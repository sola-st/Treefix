# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
ctx = self._ctx
old_device_name = ctx.device_name
old_device_spec = ctx.device_spec
new_device_name = self._device_name
cache_key = (old_device_name, new_device_name)
try:
    new_device_name, new_device_spec = _device_parsing_cache[cache_key]
except TypeError:
    # Error while trying to compute the cache key.
    raise ValueError("Expecting a string device name. Got %s(%s)" %
                     (type(new_device_name), new_device_name))
except KeyError:
    # Handle a cache miss.
    if new_device_name is not None:
        if not isinstance(new_device_name, str):
            raise ValueError("Expecting a string device name. Got %s(%s)" %
                             (type(new_device_name), new_device_name))
        device_spec = pydev.DeviceSpec.from_string(new_device_name)
        if old_device_name:
            new_device_spec = copy.copy(old_device_spec)
        else:
            ctx.ensure_initialized()
            new_device_spec = pydev.DeviceSpec.from_string(
                ctx._context_devices[0])  # pylint: disable=protected-access
        new_device_spec = new_device_spec.make_merged_spec(device_spec)
    else:
        new_device_spec = pydev.DeviceSpec.from_string("")
    new_device_name = new_device_spec.to_string()
    _device_parsing_cache[cache_key] = (new_device_name, new_device_spec)

ctx._set_device(new_device_name, new_device_spec)  # pylint: disable=protected-access
self._stack.append((old_device_name, old_device_spec, new_device_spec))
