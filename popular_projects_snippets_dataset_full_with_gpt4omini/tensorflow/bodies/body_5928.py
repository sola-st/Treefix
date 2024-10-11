# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver_test.py
os.environ['SM_HOSTS'] = '["algo-1","algo-2"]'
os.environ['SM_CURRENT_HOST'] = 'algo-2'

cluster_resolver = SageMakerClusterResolver()
self.assertEqual('algo-2:2223', cluster_resolver.master('worker', 1))
