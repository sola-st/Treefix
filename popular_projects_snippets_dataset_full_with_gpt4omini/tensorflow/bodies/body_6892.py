# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Initialize an `InputWorkers` object.

    Args:
      worker_device_pairs: A sequence of pairs: `(input device, a tuple of
        compute devices fed by that input device)`.
      canonicalize_devices: Whether to canonicalize devices for workers fully or
        partially. If False, it will partially canonicalize devices by removing
        job and task.
    """
self._worker_device_pairs = worker_device_pairs
self._input_worker_devices = tuple(d for d, _ in self._worker_device_pairs)
self._canonicalize_devices = canonicalize_devices
if canonicalize_devices:
    self._fed_devices = tuple(
        tuple(device_util.canonicalize(d)
              for d in f)
        for _, f in self._worker_device_pairs)
else:
    self._fed_devices = tuple(
        tuple(device_util.canonicalize_without_job_and_task(d)
              for d in f)
        for _, f in self._worker_device_pairs)
