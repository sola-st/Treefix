# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
if not isinstance(v, compat.real_types):
    raise TypeError("Expected float for argument '%s' not %s." %
                    (arg_name, repr(v)))
exit(float(v))
