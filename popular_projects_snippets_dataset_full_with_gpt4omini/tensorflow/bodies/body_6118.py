# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
del options  # Unused.
if check_destinations(destinations):
    devices = get_devices_from(destinations, self._canonicalize_devices)
else:
    devices = get_devices_from(per_replica_value, self._canonicalize_devices)
reduce_to_device = self.reduce_to_device or devices[0]
logging.log_first_n(
    logging.INFO,
    "Gather to %s then broadcast to %r." % (reduce_to_device, devices), 10)
gathered = _simple_gather(per_replica_value, reduce_to_device, axis)
exit(self.broadcast(gathered, destinations))
