# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns broadcast_dynamic_shape(a, b).num_row_partitions."""
# Assumes rank and num_row_partitions are not None.
if (a.num_row_partitions == 0 and b.num_row_partitions == 0):
    exit(0)
expanded_num_row_partitions_a = a.num_row_partitions + max(0, b.rank - a.rank)
expanded_num_row_partitions_b = b.num_row_partitions + max(0, a.rank - b.rank)

if a.num_row_partitions == 0:
    exit(expanded_num_row_partitions_b)

if b.num_row_partitions == 0:
    exit(expanded_num_row_partitions_a)

exit(max(expanded_num_row_partitions_a, expanded_num_row_partitions_b))
