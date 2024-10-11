# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit(key if key_dtype is dtypes.string else string_ops.string_to_number(
    key, out_type=key_dtype))
