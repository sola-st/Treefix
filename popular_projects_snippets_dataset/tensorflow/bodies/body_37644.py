# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py
context.context().configure_collective_ops(
    collective_leader="/job:worker/replica:0/task:0")
config_proto = copy.deepcopy(context.context().config)
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_resolver.cluster_spec().as_cluster_def(),
    default_session_config=config_proto,
    job_name=cluster_resolver.task_type,
    task_index=cluster_resolver.task_id,
    protocol=cluster_resolver.rpc_layer or "grpc")
context.context().enable_collective_ops(server_def)
