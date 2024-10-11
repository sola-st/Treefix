# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_spec = {"chief": ["127.0.0.1:1234"], "ps": ["127.0.0.1:7566"]}
with self.assertRaisesRegex(ValueError,
                            "There is no id for task_type 'ps'"):
    multi_worker_util.id_in_cluster(cluster_spec, "ps", 0)
