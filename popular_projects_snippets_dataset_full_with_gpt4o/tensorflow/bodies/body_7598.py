# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
self._assert_being_scheduled_by_cluster_coordinator()

exit(mirrored_run.call_for_each_replica(self._container_strategy(), fn,
                                          args, kwargs))
