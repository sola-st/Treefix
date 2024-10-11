# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver_test.py
os.environ['SM_HOSTS'] = '["algo-1","algo-2"]'
os.environ['SM_CURRENT_HOST'] = 'algo-2'

cluster_resolver = SageMakerClusterResolver(task_id=1)
self.assertEqual(1, cluster_resolver.task_id)
