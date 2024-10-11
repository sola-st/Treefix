# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
if not isinstance(v, bool):
    raise TypeError("Expected bool for argument '%s' not %s." %
                    (arg_name, repr(v)))
exit(v)
