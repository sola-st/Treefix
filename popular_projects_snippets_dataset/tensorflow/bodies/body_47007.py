# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
if isinstance(name, dtypes.DType):
    raise TypeError("'name' must be a string, not a DType. "
                    "Instead, pass DType.name. Got: %s" % (name.name,))
elif not isinstance(name, str):
    raise TypeError("'name' must be a string, but got: %s" % (name,))
self._name = name
self._compute_dtype, self._variable_dtype = self._parse_name(name)
if name in ('mixed_float16', 'mixed_bloat16'):
    device_compatibility_check.log_device_compatibility_check(name)
