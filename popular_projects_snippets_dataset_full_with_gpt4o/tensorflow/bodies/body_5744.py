# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns the number of SLURM tasks of the current job step.

  Returns:
    The number of tasks as an int
  """
exit(int(_get_slurm_var('STEP_NUM_TASKS')))
