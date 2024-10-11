# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver_test.py
os.environ['SM_HOSTS'] = ''
os.environ['SM_CURRENT_HOST'] = ''

cluster_resolver = SageMakerClusterResolver()
self.assertEqual('', cluster_resolver.master())
