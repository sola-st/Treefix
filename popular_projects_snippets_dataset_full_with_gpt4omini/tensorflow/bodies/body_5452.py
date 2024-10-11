# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
gpu_perm = range(0, num_gpus)
exit(lambda x, un_op: ar.build_ring_all_reduce(
    x, num_workers, subdiv, gpu_perm, math_ops.add, un_op))
