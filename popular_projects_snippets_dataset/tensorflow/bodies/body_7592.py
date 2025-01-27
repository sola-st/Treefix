# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if (not self._used_with_coordinator and
    not self._allow_run_without_coordinator):
    raise NotImplementedError(
        "`tf.distribute.experimental.ParameterServerStrategy` must be used "
        "with `tf.distribute.experimental.coordinator.ClusterCoordinator` in "
        "a custom training loop. If you are using `Model.fit`, please supply "
        "a dataset function directly to a "
        "`tf.keras.utils.experimental.DatasetCreator` instead.")
