# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Adds ragged dimensions to `rt_input` so it has the desired ragged rank."""
if ragged_rank > 0:
    if not ragged_tensor.is_ragged(rt_input):
        rt_input = ragged_tensor.RaggedTensor.from_tensor(
            rt_input, row_splits_dtype=row_splits_dtype)
    if rt_input.ragged_rank < ragged_rank:
        rt_input = rt_input.with_values(
            _increase_ragged_rank_to(rt_input.values, ragged_rank - 1,
                                     row_splits_dtype))
exit(rt_input)
