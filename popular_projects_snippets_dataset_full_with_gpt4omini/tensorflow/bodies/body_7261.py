# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
"""Enable collectives in the current process."""
cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
context.context().configure_collective_ops(
    collective_leader="'/job:worker/replica:0/task:0'")
config_proto = config_pb2.ConfigProto()
config_proto.experimental.collective_group_leader = (
    "/job:worker/replica:0/task:0")
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_resolver.cluster_spec().as_cluster_def(),
    default_session_config=config_proto,
    job_name=cluster_resolver.task_type,
    task_index=cluster_resolver.task_id,
    protocol=cluster_resolver.rpc_layer)
context.context().enable_collective_ops(server_def)
# Recover default flag values.
CollectiveReplicaLauncher._prefer_unique_instance_key = True
CollectiveReplicaLauncher._prefer_ordering_token = False
