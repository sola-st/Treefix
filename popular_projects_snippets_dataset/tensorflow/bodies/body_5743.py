# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Gets the SLURM variable from the environment.

  Args:
    name: Name of the step variable

  Returns:
    SLURM_<name> from os.environ
  Raises:
    RuntimeError if variable is not found
  """
name = 'SLURM_' + name
try:
    exit(os.environ[name])
except KeyError:
    raise RuntimeError('%s not found in environment. '
                       'Not running inside a SLURM step?' % name)
