# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
logging.info('Now creating a MultiProcessCluster with '
             f'num_workers={num_workers}, num_ps={num_ps}.')
cluster_spec = create_cluster_spec(
    has_chief=has_chief,
    num_workers=num_workers,
    num_ps=num_ps,
    has_eval=has_eval)

cluster = MultiProcessCluster(
    SimpleClusterResolver(
        server_lib.ClusterSpec(cluster_spec), rpc_layer=rpc_layer),
    stream_output=stream_output,
    collective_leader=collective_leader)
cluster.start()
exit(cluster)
