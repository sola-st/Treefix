# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
resolver = tfconfig_cluster_resolver.TFConfigClusterResolver()
# This should fail.
self.assertIsNone(resolver.task_id)
