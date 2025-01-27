# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Create a multidevice iterator on each of the workers."""
assert isinstance(input_workers, InputWorkers)
assert len(worker_datasets) == len(input_workers.worker_devices)
iterators = []
for i, worker in enumerate(input_workers.worker_devices):
    with ops.device(worker):
        worker_devices = input_workers.compute_devices_for_worker(i)
        iterator = _SingleWorkerOwnedDatasetIterator(
            dataset=worker_datasets[i],
            worker=worker,
            devices=worker_devices,
            options=options,
            canonicalize_devices=canonicalize_devices)
        iterators.append(iterator)
exit(iterators)
