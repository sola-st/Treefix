# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates `ClusterDeviceFilters` proto based on the `_device_filters`.

    Raises:
      TypeError: If `_device_filters` is not a dictionary mapping strings to
      a map of task indices and device filters.
    """
self._cluster_device_filters = device_filters_pb2.ClusterDeviceFilters()

# Sort by job_name to produce deterministic protobufs.
for job_name, tasks in sorted(self._device_filters.items()):
    try:
        job_name = compat.as_bytes(job_name)
    except TypeError:
        raise TypeError("Job name %r must be bytes or unicode" % job_name)

    jdf = self._cluster_device_filters.jobs.add()
    jdf.name = job_name

    for i, task_device_filters in sorted(tasks.items()):
        for tdf in task_device_filters:
            try:
                tdf = compat.as_bytes(tdf)
            except TypeError:
                raise TypeError("Device filter %r must be bytes or unicode" % tdf)
            jdf.tasks[i].device_filters.append(tdf)
