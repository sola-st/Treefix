# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = "chief"
job.tasks[0] = "127.0.0.1:1234"

job = cluster_def.job.add()
job.name = "worker"
job.tasks[0] = "127.0.0.1:8964"
job.tasks[1] = "127.0.0.1:2333"

job = cluster_def.job.add()
job.name = "ps"
job.tasks[0] = "127.0.0.1:1926"
job.tasks[1] = "127.0.0.1:3141"

self.assert_same_cluster(
    cluster_def, multi_worker_util.normalize_cluster_spec(cluster_def))
