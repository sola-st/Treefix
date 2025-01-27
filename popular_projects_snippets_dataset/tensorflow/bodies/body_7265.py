# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
"""Returns collectives and other info to be used in tests.

    Args:
      num_processes: an integer indicating the number of processes that
        participate in the collective.
      gpu_per_process: number of GPUs (0 if no GPUs) used by each process.

    Returns:
     A tuple of (collective, devices, pid) where collective is a instance
     of `CollectiveAllReduce`, devices are a list of local devices (str)
     attached to the current process, and pid is the id of this process among
     all participant processes.
    """

cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
devices = [
    "/job:worker/replica:0/task:%d/device:CPU:0" % cluster_resolver.task_id
]
if gpu_per_process > 0:
    devices = [
        "/job:worker/replica:0/task:%d/device:GPU:%d" %
        (cluster_resolver.task_id, i) for i in range(gpu_per_process)
    ]
group_size = num_processes * len(devices)
collective = cross_device_ops_lib.CollectiveAllReduce(
    devices=devices,
    group_size=group_size,
    options=collective_util.Options())
exit((collective, devices, cluster_resolver.task_id))
