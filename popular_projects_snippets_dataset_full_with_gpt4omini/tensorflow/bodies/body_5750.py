# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns a list of hostnames for nodes running the current job step."""
exit(expand_hostlist(_get_slurm_var('STEP_NODELIST')))
