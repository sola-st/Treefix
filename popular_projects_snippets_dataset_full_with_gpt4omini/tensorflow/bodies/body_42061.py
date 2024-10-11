# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
if not isinstance(v, compat.bytes_or_text_types):
    raise TypeError("Expected string for argument '%s' not %s." %
                    (arg_name, repr(v)))
exit(compat.as_bytes(v))  # Convert unicode strings to bytes.
