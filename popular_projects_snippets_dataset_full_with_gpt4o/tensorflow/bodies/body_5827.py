# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver_test.py
slurm_cluster_resolver = SlurmClusterResolver()

actual_cluster_spec = slurm_cluster_resolver.cluster_spec()
expected_proto = """
    job { name: 'worker' tasks { key: 0 value: 't02n13:8888' }
                         tasks { key: 1 value: 't02n41:8888' }
                         tasks { key: 2 value: 't02n43:8888' } }
    """
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
self.assertEqual(
    slurm_cluster_resolver.master('worker', 0, rpc_layer='grpc'),
    'grpc://t02n13:8888')
self.assertEqual(slurm_cluster_resolver.num_accelerators(), {'GPU': 1})
self.assertEqual(os.environ['CUDA_VISIBLE_DEVICES'], '0')
