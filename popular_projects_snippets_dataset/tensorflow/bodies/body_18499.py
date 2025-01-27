# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = _untile_variant(pfor_input.stacked_input(0))
exit(wrap(list_ops.tensor_list_length(handle), False))
