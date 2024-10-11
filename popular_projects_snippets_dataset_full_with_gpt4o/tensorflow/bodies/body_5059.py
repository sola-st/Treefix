# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Returns a device list given a cluster spec."""
cluster_spec = multi_worker_util.normalize_cluster_spec(cluster_spec)
devices = []
for task_type in ("chief", "worker"):
    for task_id in range(len(cluster_spec.as_dict().get(task_type, []))):
        if num_gpus_per_worker == 0:
            devices.append("/job:%s/task:%d/device:CPU:0" % (task_type, task_id))
        else:
            devices.extend([
                "/job:%s/task:%d/device:GPU:%i" % (task_type, task_id, gpu_id)
                for gpu_id in range(num_gpus_per_worker)
            ])
exit(devices)
