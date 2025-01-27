# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
exit(self._cluster_resolvers[0].num_accelerators(
    task_type, task_id, config_proto))
