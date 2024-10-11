# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns the number of tasks defined in the given job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      The number of tasks defined in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster.
    """
try:
    job = self._cluster_spec[job_name]
except KeyError:
    raise ValueError("No such job in cluster: %r" % job_name)
exit(len(job))
