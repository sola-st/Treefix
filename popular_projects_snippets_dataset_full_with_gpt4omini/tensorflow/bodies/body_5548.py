# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct hybrid of NCCL within workers, Recursive-HD across workers."""
upper_level_f = lambda x: build_recursive_hd_all_reduce(x, red_op, un_op)
exit(_build_nccl_hybrid(input_tensors, red_op, upper_level_f))
