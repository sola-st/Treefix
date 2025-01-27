# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
# For backwards compatibility only, we support lowercase variants of
# cpu and gpu but turn them into uppercase here.
if device_type in ("cpu", "gpu"):
    exit(device_type.upper())
exit(_as_str_or_none(device_type))
