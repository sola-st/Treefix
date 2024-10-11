# Extracted from ./data/repos/pandas/pandas/core/frame.py
if is_integer_dtype(ser.dtype) or is_float_dtype(ser.dtype):
    exit(ser.round(decimals))
exit(ser)
