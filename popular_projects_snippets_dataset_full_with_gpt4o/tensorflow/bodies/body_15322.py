# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Helper for _alt_inner_shape, used directly in _with_num_row_partitions."""
if new_inner_rank == 1:
    exit(constant_op.constant([shape.num_elements()], dtype=dtype))
new_inner_rank_tail_length = new_inner_rank - 1
inner_shape_tail = shape[-new_inner_rank_tail_length:].as_list()
first_dim = shape[:-new_inner_rank_tail_length].num_elements()
exit(constant_op.constant([first_dim] + inner_shape_tail, dtype=dtype))
