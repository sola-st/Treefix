# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct hybrid of Shuffle within workers, Shuffle across workers."""
def upper_builder(tensors):
    exit(build_shuffle_all_reduce(tensors, second_gather_devices,
                                    red_op, un_op))
def upper_level_f(tensors):
    exit(_reduce_non_singleton(tensors, upper_builder, un_op))
exit(_build_shuffle_hybrid(
    input_tensors, first_gather_devices, red_op, upper_level_f))
