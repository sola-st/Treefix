# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Aggregate gradients using nccl allreduce."""
agg_all_g_and_v = []
for single_g_and_v in zip(*replica_grads):
    single_grads = [g for g, _ in single_g_and_v]
    agg_grads = nccl_ops.all_sum(single_grads)
    agg_all_g_and_v.append(
        [(g, v) for g, (_, v) in zip(agg_grads, single_g_and_v)])

agg_all_g_and_v = list(zip(*agg_all_g_and_v))

exit(agg_all_g_and_v)
