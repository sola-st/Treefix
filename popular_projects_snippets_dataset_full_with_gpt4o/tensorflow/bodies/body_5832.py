# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver_test.py
slurm_cluster_resolver = SlurmClusterResolver(
    jobs={
        'ps': 1,
        'worker': 4
    },
    port_base=8888,
    gpus_per_node=4,
    gpus_per_task=2,
    auto_set_gpu=True)

actual_cluster_spec = slurm_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'ps' tasks { value: 't02n13:8888' } }
    job { name: 'worker' tasks { key: 0 value: 't02n13:8889' }
                         tasks { key: 1 value: 't02n41:8888' }
                         tasks { key: 2 value: 't02n41:8889' }
                         tasks { key: 3 value: 't02n43:8888' } }
    """

self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
assert os.environ['CUDA_VISIBLE_DEVICES'] == '2,3'
