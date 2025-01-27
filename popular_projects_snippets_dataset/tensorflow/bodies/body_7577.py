# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if coordinator_name in ["worker", "ps"]:
    raise ValueError("coordinator name should not be 'worker' or 'ps'.")
cluster_spec = self._cluster_resolver.cluster_spec()
self._num_workers = len(cluster_spec.as_dict().get("worker", ()))
self._num_ps = len(cluster_spec.as_dict().get("ps", ()))

device_filters = server_lib.ClusterDeviceFilters()
# For any worker, only the devices on ps and coordinator nodes are visible
for i in range(self._num_workers):
    device_filters.set_device_filters(
        "worker", i, ["/job:ps", "/job:%s" % coordinator_name])
# Similarly for any ps, only the devices on workers and coordinator are
# visible
for i in range(self._num_ps):
    device_filters.set_device_filters(
        "ps", i, ["/job:worker", "/job:%s" % coordinator_name])

# Allow at most one outstanding RPC for each worker at a certain time. This
# is to simplify worker failure handling in the runtime
os.environ["TF_ENABLE_EAGER_CLIENT_STREAMING_ENQUEUE"] = "False"

# Disable async executors to make context.async_wait a no-op. This avoids
# sending RPCs to remote workers since the executors used by PSStrategy
# are known to be always synchronous.
os.environ["TF_PS_DISABLE_ASYNC_EXECUTOR_GLOBALLY"] = "True"

logging.info("%s is now connecting to cluster with cluster_spec: %r",
             self.__class__.__name__, cluster_spec)
remote.connect_to_cluster(
    cluster_spec,
    job_name=coordinator_name,
    protocol=self._cluster_resolver.rpc_layer,
    cluster_device_filters=device_filters)

distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "ps_strategy_num_workers").set(self._num_workers)
distribute_lib.distribution_strategy_replica_gauge.get_cell(
    "ps_strategy_num_ps").set(self._num_ps)
