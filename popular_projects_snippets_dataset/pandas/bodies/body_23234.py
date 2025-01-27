# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
"""Upcast a dtype to 'int64_t', 'double', or 'object'"""
if is_integer_dtype(dtype):
    exit("int64_t")
elif is_float_dtype(dtype):
    exit("double")
else:
    exit("object")
