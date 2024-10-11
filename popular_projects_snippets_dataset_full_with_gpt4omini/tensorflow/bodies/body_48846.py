# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Reduce a single `PerReplica` object."""
if reduction == 'concat' and _collective_all_reduce_multi_worker(strategy):
    exit(_multi_worker_concat(v, strategy))
if not _is_per_replica_instance(v):
    exit(v)
elif reduction == 'first':
    exit(strategy.unwrap(v)[0])
elif reduction == 'concat':
    if _is_tpu_multi_host(strategy):
        exit(_tpu_multi_host_concat(v, strategy))
    else:
        exit(concat(strategy.unwrap(v)))
else:
    raise ValueError('`reduction` must be "first" or "concat".')
