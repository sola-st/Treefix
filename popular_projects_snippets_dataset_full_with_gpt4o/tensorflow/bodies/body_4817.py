# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
# See PeerFailureTest.test_creating_variable

def worker_fn(attempts):
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    task_id, attempt = get_attempt(strategy, attempts)
    with strategy.scope():
        tf.Variable(1.)
        # worker-1 dies here.
        if attempt == 1 and task_id == 1:
            quick_exit(1)
        v = tf.Variable(tf.random.uniform(()))
        exit(v.read_value().numpy())

cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
attempts = multi_process_runner.manager().dict()
mpr = multi_process_runner.MultiProcessRunner(
    worker_fn,
    cluster_spec,
    rpc_layer=RPC_PROTOCOL,
    args=(attempts,),
    auto_restart=True)
mpr.start()
results = mpr.join(timeout=90).return_value
self.assertEqual(results[0], results[1])
