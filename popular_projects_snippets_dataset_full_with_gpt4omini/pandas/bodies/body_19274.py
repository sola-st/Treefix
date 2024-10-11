# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
if is_string_or_object_np_dtype(dtype):
    exit(True)
try:
    exit(dtype == "string")
except TypeError:
    exit(False)
