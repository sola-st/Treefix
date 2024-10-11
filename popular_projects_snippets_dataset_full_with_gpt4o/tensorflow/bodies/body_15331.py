# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Unbatch a static_inner_shape when num_row_partitions > 0."""
head_dim = tensor_shape.dimension_at_index(old_shape, 0) // batch_size
exit(head_dim + old_shape[1:])
