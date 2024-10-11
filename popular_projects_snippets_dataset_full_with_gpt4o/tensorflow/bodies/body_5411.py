# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
with self.assertLogs(level="WARNING") as logs:
    exit()

self.assertIn(
    "A `tf.distribute.experimental.ParameterServerStrategy` method is "
    "invoked without using `ClusterCoordinator.schedule`. If you are not "
    "tracing a tf.function, this method is possibly executed on the "
    "coordinator, which can be slow. To properly dispatch functions to "
    "run on workers, methods like `run` or `reduce` should be used "
    "within a function passed to `tf.distribute.experimental.coordinator."
    "ClusterCoordinator.schedule`.", "".join(logs.output))
