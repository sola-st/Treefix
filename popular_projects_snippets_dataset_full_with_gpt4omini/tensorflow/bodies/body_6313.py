# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if not _creating_default_strategy_singleton:
    raise RuntimeError("Should only create a single instance of "
                       "_DefaultDistributionStrategy")
super(_DefaultDistributionStrategyV1,
      self).__init__(_DefaultDistributionExtended(self))
