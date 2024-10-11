# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
strategy = tf.distribute.MirroredStrategy(
    devices=['CPU:0', 'CPU:1', 'CPU:2'])

multiplier = np.asarray(5.)

@tf.function
def run():
    ctx = tf.distribute.get_replica_context()
    val = np.asarray(ctx.replica_id_in_sync_group)
    exit(val * multiplier)

distributed_values = strategy.run(run)
reduced = strategy.reduce(
    tf.distribute.ReduceOp.SUM, distributed_values, axis=None)

values = strategy.experimental_local_results(distributed_values)

# Note that this should match the number of virtual CPUs.
self.assertLen(values, 3)
self.assertIsInstance(values[0], np.ndarray)
self.assertIsInstance(values[1], np.ndarray)
self.assertIsInstance(values[2], np.ndarray)
self.assertAllClose(values[0], 0)
self.assertAllClose(values[1], 5)
self.assertAllClose(values[2], 10)

# "strategy.reduce" doesn't rewrap in ndarray.
# self.assertIsInstance(reduced, np.ndarray)
self.assertAllClose(reduced, 15)
