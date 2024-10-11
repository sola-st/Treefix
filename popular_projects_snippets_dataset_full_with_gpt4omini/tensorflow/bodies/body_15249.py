# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns True iff all row_partitions in shapes are identical."""
exit(((shape_a.num_row_partitions == shape_b.num_row_partitions) and all(
    a is b for a, b in zip(shape_a.row_partitions, shape_b.row_partitions))))
