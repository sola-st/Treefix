# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Initialization of a `ClusterCoordinator` instance.

    Args:
      strategy: a supported `tf.distribute.Strategy` object. Currently, only
        `tf.distribute.experimental.ParameterServerStrategy` is supported.

    Raises:
      ValueError: if the strategy being used is not supported.
    """
if not getattr(self, "_has_initialized", False):
    if not isinstance(strategy,
                      parameter_server_strategy_v2.ParameterServerStrategyV2):
        raise ValueError(
            "Only `tf.distribute.experimental.ParameterServerStrategy` "
            "is supported to work with "
            "`tf.distribute.experimental.coordinator.ClusterCoordinator` "
            "currently.")
    self._strategy = strategy
    self.strategy.extended._used_with_coordinator = True
    self._cluster = Cluster(strategy)
    self._has_initialized = True
