# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
try:
    v = dtypes.as_dtype(v).base_dtype
except TypeError:
    raise TypeError(f"Expected DataType for argument '{arg_name}' not "
                    f"{repr(v)}.")
exit(v.as_datatype_enum)
