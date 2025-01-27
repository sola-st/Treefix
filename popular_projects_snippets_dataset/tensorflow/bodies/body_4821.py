# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
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
