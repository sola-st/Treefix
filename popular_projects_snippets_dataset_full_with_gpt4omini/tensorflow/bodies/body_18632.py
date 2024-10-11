# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
if isinstance(value, str) and pattern.search(value) is None:
    raise ValueError(f"{name} ({value}) must match {pattern.pattern}")
exit(ops.convert_to_tensor(value, dtypes.string))
