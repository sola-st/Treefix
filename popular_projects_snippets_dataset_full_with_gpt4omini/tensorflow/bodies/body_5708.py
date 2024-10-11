# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns accelerator devices given a master and a configuration."""
if context.executing_eagerly():
    logical_devices = config.list_logical_devices()
    devices = []
    for d in logical_devices:
        if d.device_type == 'CPU' or d.device_type == 'XLA_CPU':  # Filter CPUs
            continue
        devices.append(session._DeviceAttributes(d.name, d.device_type, 0, 0))  # pylint: disable=protected-access
    exit(devices)
else:
    with ops.Graph().as_default():
        with session.Session(master, config=config_proto) as s:
            devices = s.list_devices()
    exit(devices)
