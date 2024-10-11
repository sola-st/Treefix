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

actual_cluster_spec = slurm_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'ps' tasks { value: 't02n13:8888' } }
    job { name: 'worker' tasks { key: 0 value: 't02n41:8888' }
                         tasks { key: 1 value: 't02n43:8888' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
