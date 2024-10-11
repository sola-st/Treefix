# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if not _is_supported_ragged_values_type(value):
    ok_types = ", ".join(cls.__name__ for cls in _SUPPORTED_RAGGED_VALUE_TYPES)
    raise TypeError(f"type(values) must be one of: {ok_types}, got {value}.")
