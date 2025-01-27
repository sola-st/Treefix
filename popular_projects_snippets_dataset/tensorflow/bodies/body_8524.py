# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
cluster_resolver = TFConfigClusterResolver()
cluster_spec = cluster_resolver.cluster_spec()
task_type = cluster_resolver.task_type
task_id = cluster_resolver.task_id
rpc_layer = cluster_resolver.rpc_layer

# TODO(yuefengz): support GPU clusters.
server_config = config_pb2.ConfigProto()
server_config.device_count['GPU'] = 0

if collective_leader:
    server_config.experimental.collective_group_leader = collective_leader
    server_config.experimental.collective_nccl = False

    logging.info(
        'Enabling collective ops with cluster_spec = %r, task_type = %r, '
        'task_id = %r, rpc_layer = %r, collective_leader = %s',
        cluster_spec, task_type, task_id, rpc_layer, collective_leader)
else:
    logging.info(
        'Starting server with cluster_spec = %r, task_type = %r, '
        'task_id = %r, rpc_layer = %r', cluster_spec, task_type, task_id,
        rpc_layer)

server_lib.Server(
    cluster_spec,
    job_name=task_type,
    protocol=rpc_layer,
    task_index=task_id,
    config=server_config,
    start=True)

start_event = start_events[task_type][task_id]
start_event.set()

finish_event = finish_events[task_type][task_id]
finish_event.wait()

os._exit(0)  # pylint: disable=protected-access
