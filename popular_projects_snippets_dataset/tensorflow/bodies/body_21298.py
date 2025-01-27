# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
cluster_def = cluster_pb2.ClusterDef()
job = cluster_def.job.add()
job.name = "master"
job.tasks[0] = master.target[len("grpc://"):]
job = cluster_def.job.add()
job.name = "worker"
job.tasks[0] = worker.target[len("grpc://"):]
exit(cluster_def)
