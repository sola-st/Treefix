# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
exit(mirrored_run.call_for_each_replica(
    self._container_strategy(), fn, args, kwargs))
