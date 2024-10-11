# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if dtypes.string == tensor.dtype.base_dtype:
    exit(tensor)
exit(string_ops.as_string(tensor))
