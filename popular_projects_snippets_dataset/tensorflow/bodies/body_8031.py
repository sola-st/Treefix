# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, _ = create_test_objects(
    cluster_spec=self._cluster_spec,
    task_type='worker',
    task_id=0,
    num_gpus=2)
num_workers = len(self._cluster_spec.get('chief', []) +
                  self._cluster_spec.get('worker', []))
self.assertEqual(2 * num_workers,
                 distribution.num_replicas_in_sync)
