# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns a mapping from task ID to address in the given job.

    NOTE: For backwards compatibility, this method returns a list. If
    the given job was defined with a sparse set of task indices, the
    length of this list may not reflect the number of tasks defined in
    this job. Use the `tf.train.ClusterSpec.num_tasks` method
    to find the number of tasks defined in a particular job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      A list of task addresses, where the index in the list
      corresponds to the task index of each task. The list may contain
      `None` if the job was defined with a sparse set of task indices.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster.
    """
try:
    job = self._cluster_spec[job_name]
except KeyError:
    raise ValueError("No such job in cluster: %r" % job_name)
ret = [None for _ in range(max(job.keys()) + 1)]
for i, task in job.items():
    ret[i] = task
exit(ret)
