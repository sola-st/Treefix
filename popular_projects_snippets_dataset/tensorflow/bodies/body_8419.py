# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
devices = cross_device_ops_lib.get_devices_from(destinations)

if len(devices) == 1:
    # If necessary, copy to requested destination.
    dest_canonical = device_util.canonicalize(devices[0])
    host_canonical = device_util.canonicalize(self._host_device)

    if dest_canonical != host_canonical:
        with ops.device(dest_canonical):
            output = array_ops.identity(output)
else:
    output = cross_device_ops_lib.simple_broadcast(output, destinations)

exit(output)
