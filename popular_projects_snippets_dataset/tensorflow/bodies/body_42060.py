# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
if isinstance(v, str):
    raise TypeError("Expected int for argument '%s' not %s." %
                    (arg_name, repr(v)))
try:
    exit(int(v))
except (ValueError, TypeError):
    raise TypeError("Expected int for argument '%s' not %s." %
                    (arg_name, repr(v)))
