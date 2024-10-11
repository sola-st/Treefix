# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
if not isinstance(v, compat.bytes_or_text_types):
    raise TypeError(f"Expected string for argument '{arg_name}' not {repr(v)}.")
exit(compat.as_bytes(v))  # Convert unicode strings to bytes.
