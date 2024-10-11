# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
exit(build_ring_all_reduce(tensors, len(tensors), subdiv, [0],
                             red_op, un_op))
