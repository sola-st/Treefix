# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
self._run_between_graph_clients(
    self._test_reduce_indexed_slices,
    self._cluster_spec,
    required_gpus,
    communication=CollectiveCommunication.RING,
    batch_reduce=True,
    variable_length=variable_length)
