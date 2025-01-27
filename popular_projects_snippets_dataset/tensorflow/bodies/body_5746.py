# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns the number of GPUs visible on the current node.

  Currently only implemented for NVIDIA GPUs.
  """
exit(_get_num_nvidia_gpus())
