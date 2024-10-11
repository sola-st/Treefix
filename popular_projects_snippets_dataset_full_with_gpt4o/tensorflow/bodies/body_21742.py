# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates a `tf.train.ClusterDef` based on the given `cluster_spec`.

    Raises:
      TypeError: If `cluster_spec` is not a dictionary mapping strings to lists
        of strings.
    """
self._cluster_def = cluster_pb2.ClusterDef()

# NOTE(mrry): Sort by job_name to produce deterministic protobufs.
for job_name, tasks in sorted(self._cluster_spec.items()):
    try:
        job_name = compat.as_bytes(job_name)
    except TypeError:
        raise TypeError("Job name %r must be bytes or unicode" % job_name)

    job_def = self._cluster_def.job.add()
    job_def.name = job_name

    for i, task_address in sorted(tasks.items()):
        try:
            task_address = compat.as_bytes(task_address)
        except TypeError:
            raise TypeError("Task address %r must be bytes or unicode" %
                            task_address)
        job_def.tasks[i] = task_address
