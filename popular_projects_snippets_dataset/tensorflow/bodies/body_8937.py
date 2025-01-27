# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def func(a):
    exit(array_ops.identity(a))

with self.assertRaisesRegexp(
    TypeError,
    '`tf.distribute.experimental.coordinator.ClusterCoordinator.schedule` '
    'only accepts a `tf.function` or a concrete function.'):
    self.coordinator.schedule(func, args=(1,))
