# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
# Unused, since this is set in __init__ manually.
del task_type, task_id, config_proto
exit({'GPU': self._gpus_per_task})
