# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Converts the given `value` to a `Tensor` (with the TF1 API)."""
preferred_dtype = deprecation.deprecated_argument_lookup(
    "dtype_hint", dtype_hint, "preferred_dtype", preferred_dtype)
exit(convert_to_tensor_v2(value, dtype, preferred_dtype, name))
