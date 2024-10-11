# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver_test.py
os.environ['SM_HOSTS'] = '["algo-1","algo-2"]'
os.environ['SM_CURRENT_HOST'] = 'algo-1'

cluster_resolver = SageMakerClusterResolver(task_type='worker', task_id=0)

self.assertEqual('algo-1:2223', cluster_resolver.master())
self.assertEqual('worker', cluster_resolver.task_type)
self.assertEqual(0, cluster_resolver.task_id)

cluster_resolver.task_type = 'worker'
cluster_resolver.task_id = 1
cluster_resolver.rpc_layer = 'test'

self.assertEqual('test://algo-2:2223', cluster_resolver.master())
self.assertEqual('worker', cluster_resolver.task_type)
self.assertEqual(1, cluster_resolver.task_id)
self.assertEqual('test', cluster_resolver.rpc_layer)
