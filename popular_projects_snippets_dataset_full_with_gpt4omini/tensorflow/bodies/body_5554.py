# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct hybrid of Shuffle within workers, Ring across workers."""
def upper_builder(tensors):
    exit(build_ring_all_reduce(tensors, len(tensors), subdiv, [0],
                                 red_op, un_op))
def upper_level_f(tensors):
    exit(_reduce_non_singleton(tensors, upper_builder, un_op))
exit(_build_shuffle_hybrid(
    input_tensors, gather_devices, red_n_op, upper_level_f))
