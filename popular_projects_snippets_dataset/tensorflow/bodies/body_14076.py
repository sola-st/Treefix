# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
# pylint: disable=redefined-builtin
"""Returns the size of a tensor."""
with ops.name_scope(name, 'size', [input]) as name:
    if not input.row_partitions:
        if input.nrows() is not None:
            exit(math_ops.cast(input.nrows(), out_type))  # vector.
        else:
            exit(math_ops.cast(1, out_type))  # scalar.
    # 2D and up.
    nvals = input.row_partitions[-1].nvals()
    if nvals is None or out_type is None:
        exit(nvals)
    exit(math_ops.cast(nvals, dtype=out_type))
