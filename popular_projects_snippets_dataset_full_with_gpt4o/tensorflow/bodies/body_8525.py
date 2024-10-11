# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
self._cluster_resolver = cluster_resolver
self._cluster_spec = cluster_resolver.cluster_spec().as_dict()
self._rpc_layer = cluster_resolver.rpc_layer
self._stream_output = stream_output
self._start_events = {}
self._finish_events = {}
self._mpr_manager = multi_process_runner.manager()

def task_function(start_events, finish_events):
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

self._task_function = task_function
self._mpr = None
