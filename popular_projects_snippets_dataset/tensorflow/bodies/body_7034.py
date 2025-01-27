# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
tf_config = cluster_resolver.TFConfigClusterResolver()
master = tf_config.master()
if tf_config.rpc_layer:
    # Strip off the rpc_layer suffix.
    master = master[len("%s://" % tf_config.rpc_layer):]
resolver = cluster_resolver.SimpleClusterResolver(
    cluster_spec=tf_config.cluster_spec(),
    task_type=tf_config.task_type,
    task_id=tf_config.task_id,
    master=master,
    environment=tf_config.environment,
    num_accelerators={"GPU": required_gpus},
    rpc_layer=tf_config.rpc_layer or "grpc",
)
# Disable health check and coordination service. We don't have a reliable
# way to shutdown the strategy (and thus the strategy health check or
# coordination service heartbeat) at the end of a test. Turning on the
# strategy health check or coordination service heartbeat causes some
# flakiness since we re-create part of the server when creating a strategy,
# and our tests are capable of handling failures.
CollectiveAllReduceExtended._enable_check_health = False  # pylint: disable=protected-access
context.context().configure_coordination_service(service_type="")
# Always create the strategy in eager mode so that it starts the server and
# configures the eager context. The eager context can no longer be
# configured after initialization.
with context.eager_mode():
    strategy = CollectiveAllReduceStrategy(cluster_resolver=resolver)

if not use_merge_call:
    strategy.extended._use_merge_call = lambda: False  # pylint: disable=protected-access
# TODO(b/152320929): Wait for the cluster before proceeding, otherwise
# collectives may hang if any worker launches collectives before the chief
# creates the strategy.
try:
    multi_process_runner.get_barrier().wait()
except ValueError:
    # If the creator is called in the main process,
    # multi_process_runner.get_barrier() raises ValueError, which is safe to
    # ignore.
    pass
exit(strategy)
