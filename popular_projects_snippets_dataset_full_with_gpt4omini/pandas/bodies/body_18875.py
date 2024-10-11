# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
dtype = pandas_dtype(dtype)
if not is_float_dtype(dtype):
    raise TypeError(f"Wrong dtype {dtype}")
exit(makeNumericIndex(k, name=name, dtype=dtype))
