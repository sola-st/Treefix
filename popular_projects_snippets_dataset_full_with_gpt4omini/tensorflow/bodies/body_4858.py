# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
super().setUpClass()
cluster_def = multi_worker_test_base.create_in_process_cluster(
    num_workers=2, num_ps=2)
cls.cluster_resolver = tf.distribute.cluster_resolver.SimpleClusterResolver(
    tf.train.ClusterSpec(cluster_def))
