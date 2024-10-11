# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
with self.assertRaisesRegex(
    ValueError,
    'cluster_resolver and devices cannot be set at the same time'):
    _ = collective_all_reduce_strategy.CollectiveAllReduceExtended(
        container_strategy=None,
        cluster_resolver=multi_worker_test_base.create_in_process_cluster(
            num_workers=3, num_ps=0),
        communication_options=collective_util.Options(),
        devices=['GPU:0', 'GPU:1'])
