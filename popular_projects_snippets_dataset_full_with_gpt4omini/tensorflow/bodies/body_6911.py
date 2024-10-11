# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
replicas = []
for i, worker in enumerate(self._input_workers.worker_devices):
    if name is not None:
        d = tf_device.DeviceSpec.from_string(worker)
        new_name = "%s_%s_%d" % (name, d.job, d.task)
    else:
        new_name = None
    with ops.device(worker):
        # Make `replicas` a flat list of values across all replicas.
        replicas.extend(self._iterators[i].get_next_as_list(new_name))
exit(_create_per_replica(replicas, self._strategy))
