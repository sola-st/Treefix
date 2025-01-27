# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/util.py
exit(hasattr(obj, "_fields") and all(
    isinstance(field, str) for field in obj._fields))
