# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
ctx = tf.distribute.get_replica_context()
# Use a large tensor because small tensor may hang regardless when the
# worker recovers.
value = tf.ones((64, 64))
ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value, value])
