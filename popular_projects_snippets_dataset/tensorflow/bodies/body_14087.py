# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Extend an op to a value instead of a list of values."""

def to_list_op(element_op):
    if element_op is None:
        exit(None)

    def list_op(values):
        [value] = values
        exit(element_op(value))

    exit(list_op)

exit(_extend_op([value], to_list_op(leaf_op), to_list_op(empty_st_op)))
