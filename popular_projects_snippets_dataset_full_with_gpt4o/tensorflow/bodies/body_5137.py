# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = ["127.0.0.1:8964", "127.0.0.1:2333"]

with self.assertRaisesRegex(
    ValueError,
    "`cluster_spec' should be dict or a `tf.train.ClusterSpec` or a "
    "`tf.train.ClusterDef` object"):
    multi_worker_util.normalize_cluster_spec(cluster_spec)
