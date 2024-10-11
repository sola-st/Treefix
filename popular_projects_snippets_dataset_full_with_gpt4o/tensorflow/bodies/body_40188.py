# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
"""Returns a server def with a single job + multiple tasks."""
cluster_def = cluster_pb2.ClusterDef()
job_def = cluster_def.job.add()
job_def.name = job_name
job_def.tasks[0] = "localhost:%d" % local_server_port

for i, remote_server_address in enumerate(remote_server_addresses, start=1):
    job_def.tasks[i] = remote_server_address

server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def,
    job_name=job_name,
    task_index=task_index,
    protocol="grpc")

exit(server_def)
