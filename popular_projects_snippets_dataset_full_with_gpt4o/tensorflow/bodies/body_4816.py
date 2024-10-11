# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
task_id, attempt = get_attempt(strategy, attempts)
with strategy.scope():
    tf.Variable(1.)
    # worker-1 dies here.
    if attempt == 1 and task_id == 1:
        quick_exit(1)
    v = tf.Variable(tf.random.uniform(()))
    exit(v.read_value().numpy())
