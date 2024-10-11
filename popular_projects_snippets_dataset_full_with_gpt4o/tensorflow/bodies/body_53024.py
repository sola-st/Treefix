# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
if not nest.is_nested(value):
    exit(value)
exit(tuple([_as_tuple(v) for v in value]))
