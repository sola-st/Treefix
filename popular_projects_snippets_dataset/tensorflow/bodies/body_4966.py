# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
super().setUp()
cluster_def = get_cluster_def(test_cluster_params, num_workers=2, num_ps=3)
self.cluster_resolver = SimpleClusterResolver(ClusterSpec(cluster_def))
