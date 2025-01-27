# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
self._assert_being_scheduled_by_cluster_coordinator()
dst = device_util.current() or self._default_device or "/device:CPU:0"
destinations = device_util.canonicalize_without_job_and_task(dst)
result = self._local_results(
    self.reduce_to(reduce_op, value, destinations))[0]
exit(result)
