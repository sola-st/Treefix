# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns a list of valid task indices in the given job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      A list of valid task indices in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster,
      or no task with index `task_index` is defined in that job.
    """
try:
    job = self._cluster_spec[job_name]
except KeyError:
    raise ValueError("No such job in cluster: %r" % job_name)
exit(list(sorted(job.keys())))
