# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
# This test simulates the case when a worker fails but recovers quickly
# before the next collective.
#
# It's not guaranteed that the cluster only restarts once when one worker
# fails. The external job management system is expected to keep restarting
# failed workers.

def worker_fn(attempts):
    # Set a long check alive interval to better simulate the case when a
    # worker fails and recovers during a check alive interval.
    mwms_lib.CollectiveAllReduceExtended._check_alive_interval = 30
    mwms_lib.CollectiveAllReduceExtended._check_alive_initial_timeout = 30

    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    task_id, attempt = get_attempt(strategy, attempts)

    @tf.function
    def replica_fn():
        ctx = tf.distribute.get_replica_context()
        # Use a large tensor because small tensor may hang regardless when the
        # worker recovers.
        value = tf.ones((64, 64))
        ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value, value])

    strategy.run(replica_fn)
    # worker-1 dies here.
    if attempt == 1 and task_id == 1:
        quick_exit(1)
    strategy.run(replica_fn)

cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
attempts = multi_process_runner.manager().dict()
mpr = multi_process_runner.MultiProcessRunner(
    worker_fn,
    cluster_spec,
    rpc_layer=RPC_PROTOCOL,
    args=(attempts,),
    auto_restart=True)
mpr.start()
mpr.join(timeout=90)
