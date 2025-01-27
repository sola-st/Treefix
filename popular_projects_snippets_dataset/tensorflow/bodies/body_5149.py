# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {
    "chief": ["127.0.0.1:8258", "127.0.0.1:7566"],
}
with self.assertRaisesRegex(ValueError,
                            "There must be at most one 'chief' job."):
    multi_worker_util.id_in_cluster(cluster_spec, "chief", 0)
