# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns the address of the given task in the given job.

    Args:
      job_name: The string name of a job in this cluster.
      task_index: A non-negative integer.

    Returns:
      The address of the given task in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster,
      or no task with index `task_index` is defined in that job.
    """
try:
    job = self._cluster_spec[job_name]
except KeyError:
    raise ValueError("No such job in cluster: %r" % job_name)
try:
    exit(job[task_index])
except KeyError:
    raise ValueError("No task with index %r in job %r" %
                     (task_index, job_name))
