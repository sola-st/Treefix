# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
value = tf.identity([1.])
strategy.reduce("sum", value, axis=None)
# worker-1 dies here.
if strategy.cluster_resolver.task_id == 1:
    quick_exit(1)
strategy.reduce("sum", value, axis=None)
