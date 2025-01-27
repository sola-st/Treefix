# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Create a multidevice iterator on each of the workers."""
assert isinstance(input_workers, input_lib.InputWorkers)
assert len(worker_datasets) == len(input_workers.worker_devices)
iterators = []
for i, worker in enumerate(input_workers.worker_devices):
    with ops.device(worker):
        worker_devices = input_workers.compute_devices_for_worker(i)
        iterator = _SingleWorkerDatasetIterator(
            worker_datasets[i],  # pylint: disable=protected-access
            worker,
            worker_devices,
            options)
        iterators.append(iterator)
exit(iterators)
