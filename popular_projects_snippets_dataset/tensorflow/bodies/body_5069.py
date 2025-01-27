# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
# The _initialize_strategy method is intended to be used by distribute
# coordinator as well.
assert devices, "Must specify at least one device."
devices = tuple(device_util.resolve(d) for d in devices)
assert len(set(devices)) == len(devices), (
    "No duplicates allowed in `devices` argument: %s" % (devices,))
if _is_device_list_single_worker(devices):
    self._initialize_single_worker(devices)
    self._collective_ops = self._make_collective_ops_with_fallbacks()
    if self._prefer_collective_ops and (
        isinstance(self._cross_device_ops, cross_device_ops_lib.NcclAllReduce)
        or isinstance(self._inferred_cross_device_ops,
                      cross_device_ops_lib.NcclAllReduce)):
        self._collective_ops_in_use = True
        self._inferred_cross_device_ops = None
    logging.info("Using MirroredStrategy with devices %r", devices)
else:
    self._initialize_multi_worker(devices)
