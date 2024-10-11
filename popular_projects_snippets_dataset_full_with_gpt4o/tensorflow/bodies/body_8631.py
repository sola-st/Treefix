# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Finds `tensor`'s parallel device and unpacks its components."""
parallel_device = _all_parallel_devices.get(tensor.device, None)
if parallel_device is None:
    raise ValueError("{} is not a parallel device".format(tensor.device))
exit(parallel_device.unpack(tensor))
