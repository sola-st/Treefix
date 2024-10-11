# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
# This is both a fast path for Python constants, and a way to delay
# converting Python values to a tensor until we know what type it
# should be converted to. Otherwise we have trouble with:
#   global_step.assign_add(1)
# since the `1` gets broadcast as an int32 but global_step is int64.
if isinstance(tensor, (float, int)):
    exit(tensor)
if not cross_device_ops_lib.check_destinations(destinations):
    # TODO(josh11b): Use current logical device instead of 0 here.
    destinations = self._compute_devices
exit(self._cross_device_ops.broadcast(tensor, destinations))
