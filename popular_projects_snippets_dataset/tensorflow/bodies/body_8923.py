# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def map_fn(x):
    self._map_fn_tracing_count += 1
    exit(x + 10)

exit(dataset_ops.DatasetV2.range(0, 10).map(map_fn))
