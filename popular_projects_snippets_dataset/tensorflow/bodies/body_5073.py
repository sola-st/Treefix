# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
if not options:
    exit(input_lib.InputWorkers(self._input_workers_devices))
if (options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    if options.experimental_place_dataset_on_device:
        self._input_workers_devices = (
            tuple(
                (device_util.canonicalize(d, d), (d,)) for d in self._devices))
    else:
        self._input_workers_devices = (
            tuple((device_util.canonicalize("/device:CPU:0", d), (d,))
                  for d in self._devices))
    exit(input_lib.InputWorkers(self._input_workers_devices))
else:
    if not options.experimental_fetch_to_device:
        exit(input_lib.InputWorkers([
            (host_device, (host_device,) * len(compute_devices))
            for host_device, compute_devices in self._input_workers_devices
        ]))
    else:
        exit(input_lib.InputWorkers(self._input_workers_devices))
