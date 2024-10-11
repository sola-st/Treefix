# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
"""Initializes this strategy with an optional `cluster_resolver`.

    Args:
      cluster_resolver: Optional
        `tf.distribute.cluster_resolver.ClusterResolver` object. Defaults to a
        `tf.distribute.cluster_resolver.TFConfigClusterResolver`.
    """
if cluster_resolver is None:
    cluster_resolver = TFConfigClusterResolver()
super(ParameterServerStrategyV1, self).__init__(
    ParameterServerStrategyExtended(
        self, cluster_resolver=cluster_resolver))
distribute_lib.distribution_strategy_gauge.get_cell("V1").set(
    "ParameterServerStrategy")
