# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if not isinstance(v, bool):
    raise TypeError(f"Expected bool for argument '{arg_name}' not {repr(v)}.")
exit(v)
