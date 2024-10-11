# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct hybrid of NCCL within workers, Shuffle across workers."""
def upper_level_f(x):
    exit(build_shuffle_all_reduce(x, gather_devices, shuffle_red_op, un_op))

exit(_build_nccl_hybrid(input_tensors, nccl_red_op, upper_level_f))
