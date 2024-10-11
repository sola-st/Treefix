# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if not isinstance(v, compat.real_types):
    raise TypeError(f"Expected float for argument '{arg_name}' not {repr(v)}.")
exit(float(v))
