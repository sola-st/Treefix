# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
self._run_between_graph_clients(
    self._test_variable_initialization,
    self._cluster_spec,
    num_gpus=required_gpus)
