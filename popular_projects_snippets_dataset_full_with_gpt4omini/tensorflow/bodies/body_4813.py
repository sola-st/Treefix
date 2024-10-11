# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
# This test simulates the case when a worker fails before or during creating
# a variable. Creating variables involve broadcasting the initial value from
# the first replica to all replicas.

def worker_fn():
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    with strategy.scope():
        tf.Variable(1.)
        # worker-1 dies here.
        if strategy.cluster_resolver.task_id == 1:
            quick_exit(1)
        v = tf.Variable(tf.random.uniform(()))
        exit(v.read_value().numpy())

cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
mpr = multi_process_runner.MultiProcessRunner(
    worker_fn, cluster_spec, rpc_layer=RPC_PROTOCOL)
mpr.start()
# TODO(b/151232436): Always raise UnavailableError when a peer fails.
with self.assertRaises(
    (tf.errors.UnavailableError, tf.errors.DeadlineExceededError)):
    mpr.join(timeout=60)
