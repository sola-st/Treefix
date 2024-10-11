# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if not isinstance(communication_options, collective_util.Options):
    raise ValueError("communication_options must be an instance of "
                     "tf.distribute.experimental.CommunicationOptions")
if cluster_resolver and devices:
    raise ValueError(
        "cluster_resolver and devices cannot be set at the same time")

self._cluster_resolver = cluster_resolver or TFConfigClusterResolver()
if not isinstance(self._cluster_resolver, ClusterResolver):
    raise ValueError("cluster_resolver must be an instance of "
                     "tf.distribute.cluster_resolver.ClusterResolver")
distribute_lib.StrategyExtendedV1.__init__(self, container_strategy)
self._communication_options = communication_options
self._collective_key_base = container_strategy._collective_key_base  # pylint: disable=protected-access
self._initialize_strategy(self._cluster_resolver, devices=devices)
self._cfer_fn_cache = weakref.WeakKeyDictionary()
self.experimental_enable_get_next_as_optional = True
assert isinstance(self._cross_device_ops,
                  cross_device_ops_lib.CollectiveAllReduce)
