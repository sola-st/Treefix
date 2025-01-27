# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
updated_config = copy.deepcopy(config_proto)
updated_config.isolate_session_state = True
cluster_spec = self._tpu_cluster_resolver.cluster_spec()
if cluster_spec:
    updated_config.cluster_def.CopyFrom(cluster_spec.as_cluster_def())
exit(updated_config)
