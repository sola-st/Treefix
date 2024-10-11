# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver_test.py
slurm_cluster_resolver = SlurmClusterResolver(
    jobs={
        'ps': 1,
        'worker': 2
    },
    port_base=8888,
    tasks_per_node=1,
    gpus_per_node=1,
    gpus_per_task=1,
    auto_set_gpu=False)

slurm_cluster_resolver.task_type = 'worker'
slurm_cluster_resolver.task_id = 1
self.assertEqual(slurm_cluster_resolver.master(), 'grpc://t02n43:8888')

slurm_cluster_resolver.rpc_layer = 'ab'
self.assertEqual(slurm_cluster_resolver.master('ps', 0), 'ab://t02n13:8888')
self.assertEqual(
    slurm_cluster_resolver.master('ps', 0, rpc_layer='test'),
    'test://t02n13:8888')
