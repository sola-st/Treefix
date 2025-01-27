# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
cluster_spec = server_lib.ClusterSpec(
    multi_worker_test_base.create_cluster_spec(
        has_chief=False, num_workers=1, num_ps=0, has_eval=False))
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_spec.as_cluster_def(),
    job_name="worker",
    task_index=0,
    protocol="grpc",
    port=0)
context.context().enable_collective_ops(server_def)
self.assertEqual(
    device_util.canonicalize("/cpu:0"),
    "/job:worker/replica:0/task:0/device:CPU:0")
