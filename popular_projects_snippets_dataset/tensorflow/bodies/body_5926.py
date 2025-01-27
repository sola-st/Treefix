# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver_test.py
os.environ['SM_HOSTS'] = '["algo-1","algo-2"]'
os.environ['SM_CURRENT_HOST'] = 'algo-2'

cluster_resolver = SageMakerClusterResolver()
expected_proto = """
    job { name: 'worker' tasks { key: 0 value: 'algo-1:2223' }
                         tasks { key: 1 value: 'algo-2:2223' } }
    """
actual_cluster_spec = cluster_resolver.cluster_spec()
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
