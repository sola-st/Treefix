# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Return a list of devices for each worker in the system."""
devices = session.list_devices()

devices_that_support_heartbeats = []

for device in devices:
    name = device.name
    # Pick devices that have a TPU but target the attached CPU
    if ':TPU:0' in name and 'coordinator' not in name:
        devices_that_support_heartbeats.append(name.replace('TPU', 'CPU'))

exit(devices_that_support_heartbeats)
