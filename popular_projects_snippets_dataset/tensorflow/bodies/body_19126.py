# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
not_none = dimension_size is not None
try:
    int(dimension_size)
    can_be_parsed_as_int = True
except (ValueError, TypeError):
    can_be_parsed_as_int = False
exit(not_none and can_be_parsed_as_int)
