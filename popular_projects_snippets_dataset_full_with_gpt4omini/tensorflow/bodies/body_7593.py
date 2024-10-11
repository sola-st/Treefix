# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if not self._being_scheduled and not self._allow_run_without_coordinator:
    logging.warning(
        "A `tf.distribute.experimental.ParameterServerStrategy` method is "
        "invoked without using `ClusterCoordinator.schedule`. If you are not "
        "tracing a tf.function, this method is possibly executed on the "
        "coordinator, which can be slow. To properly dispatch functions to "
        "run on workers, methods like `run` or `reduce` should be used "
        "within a function passed to `tf.distribute.experimental.coordinator."
        "ClusterCoordinator.schedule`.")
