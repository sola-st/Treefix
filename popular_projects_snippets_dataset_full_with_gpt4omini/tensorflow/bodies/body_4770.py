# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
exit(mirrored_run.call_for_each_replica(self._container_strategy(), fn,
                                          args, kwargs))
