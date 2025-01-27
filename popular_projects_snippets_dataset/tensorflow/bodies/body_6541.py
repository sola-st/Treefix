# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
exit(math_ops.cast(_replica_id() + 1, dtype=dtypes.float32))
