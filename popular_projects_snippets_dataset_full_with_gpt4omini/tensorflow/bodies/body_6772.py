# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(
    cluster_spec=self._cluster_spec,
    task_type='worker',
    task_id=1,
    num_gpus=0)
self.assertTrue(strategy.extended._in_multi_worker_mode())
