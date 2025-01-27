# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct hybrid of NCCL within workers, Ring across workers."""
def upper_builder(y):
    exit(build_ring_all_reduce(y, len(y), subdiv, [0], red_op, un_op))
def upper_level_f(x):
    exit(_reduce_non_singleton(x, upper_builder, un_op))
exit(_build_nccl_hybrid(input_tensors, red_op, upper_level_f))
