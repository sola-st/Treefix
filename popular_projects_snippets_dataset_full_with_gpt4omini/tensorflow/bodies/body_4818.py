# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
task_id, attempt = get_attempt(strategy, attempts)
value = tf.identity([1.])
strategy.reduce("sum", value, axis=None)
# worker-1 dies here.
if attempt == 1 and task_id == 1:
    quick_exit(1)
exit(strategy.reduce("sum", value, axis=None).numpy())
