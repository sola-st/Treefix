# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
updated_config = copy.deepcopy(config_proto)
if not self._cluster_spec:
    updated_config.isolate_session_state = True
    exit(updated_config)

updated_config.isolate_session_state = False

assert self._task_type
assert self._task_id is not None

# The device filters prevent communication between workers.
del updated_config.device_filters[:]
if self._task_type in ["chief", "worker"]:
    updated_config.device_filters.extend(
        ["/job:%s/task:%d" % (self._task_type, self._task_id), "/job:ps"])
elif self._task_type == "evaluator":
    updated_config.device_filters.append(
        "/job:%s/task:%d" % (self._task_type, self._task_id))
exit(updated_config)
