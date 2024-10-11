# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns the rank of the current task in range [0, num_tasks)."""
exit(int(_get_slurm_var('PROCID')))
