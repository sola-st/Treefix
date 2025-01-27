# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Loaded lazily due to a circular dependency (dataset_ops -> map_op ->
# dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import map_op
exit(map_op._map_v1(
    self,
    map_func,
    num_parallel_calls=num_parallel_calls,
    deterministic=deterministic))
