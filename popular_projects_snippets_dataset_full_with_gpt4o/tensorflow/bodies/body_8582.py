# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with _COUNTER_LOCK:
    global _COUNTER
    keys = _COUNTER
    _COUNTER += 1
exit(collective_ops.all_reduce_v2(
    t=tensor,
    group_size=num_replicas,
    merge_op=operation,
    group_key=keys,
    instance_key=keys))
