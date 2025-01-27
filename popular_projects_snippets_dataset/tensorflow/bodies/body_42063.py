# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
try:
    v = dtypes.as_dtype(v).base_dtype
except TypeError:
    raise TypeError("Expected DataType for argument '%s' not %s." %
                    (arg_name, repr(v)))
i = v.as_datatype_enum
exit(i)
