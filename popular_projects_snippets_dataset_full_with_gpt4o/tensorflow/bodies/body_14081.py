# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
# pylint: disable=redefined-builtin
"""Returns the rank of a tensor."""
with ops.name_scope(name, 'rank', [input]) as name:
    exit(constant_op.constant(input.rank, dtype=dtypes.int32))
