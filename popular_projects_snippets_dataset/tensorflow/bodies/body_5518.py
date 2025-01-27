# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
hints = collective_util.Hints(bytes_per_pack=bytes_per_pack)
self._run_between_graph_clients(
    self._test_reduction,
    self._cluster_spec,
    required_gpus,
    communication=CollectiveCommunication.RING,
    use_strategy_object=use_strategy_object,
    hints=hints)
