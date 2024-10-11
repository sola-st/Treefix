# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
del cluster_spec, task_type, task_id
if session_config:
    session_config.CopyFrom(self._update_config_proto(session_config))
