# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates a `ClusterSpec`.

    Args:
      cluster: A dictionary mapping one or more job names to (i) a list of
        network addresses, or (ii) a dictionary mapping integer task indices to
        network addresses; or a `tf.train.ClusterDef` protocol buffer.

    Raises:
      TypeError: If `cluster` is not a dictionary mapping strings to lists
        of strings, and not a `tf.train.ClusterDef` protobuf.
    """
if isinstance(cluster, dict):
    self._cluster_spec = {}
    for job_name, tasks in cluster.items():
        if isinstance(tasks, (list, tuple)):
            job_tasks = {i: task for i, task in enumerate(tasks)}
        elif isinstance(tasks, dict):
            job_tasks = {int(i): task for i, task in tasks.items()}
        else:
            raise TypeError("The tasks for job %r must be a list or a dictionary "
                            "from integers to strings." % job_name)
        self._cluster_spec[job_name] = job_tasks
    self._make_cluster_def()
elif isinstance(cluster, cluster_pb2.ClusterDef):
    self._cluster_def = cluster
    self._cluster_spec = {}
    for job_def in self._cluster_def.job:
        self._cluster_spec[job_def.name] = {
            i: t for i, t in job_def.tasks.items()
        }
elif isinstance(cluster, ClusterSpec):
    self._cluster_def = cluster_pb2.ClusterDef()
    self._cluster_def.MergeFrom(cluster.as_cluster_def())
    self._cluster_spec = {}
    for job_def in self._cluster_def.job:
        self._cluster_spec[job_def.name] = {
            i: t for i, t in job_def.tasks.items()
        }
else:
    raise TypeError("`cluster` must be a dictionary mapping one or more "
                    "job names to lists of network addresses, or a "
                    "`ClusterDef` protocol buffer")
