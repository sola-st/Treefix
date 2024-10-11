# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
exit(t if isinstance(t, type_spec.TypeSpec) else dtypes.as_dtype(t))
