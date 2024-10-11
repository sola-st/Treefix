# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
self._run_between_graph_clients(self._test_simple_increment,
                                self._cluster_spec, context.num_gpus())
