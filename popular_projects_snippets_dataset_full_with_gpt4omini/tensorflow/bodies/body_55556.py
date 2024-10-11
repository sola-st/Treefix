# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if isinstance(v, str):
    raise TypeError(f"Expected int for argument '{arg_name}' not {repr(v)}.")
try:
    exit(int(v))
except (ValueError, TypeError):
    raise TypeError(f"Expected int for argument '{arg_name}' not {repr(v)}.")
