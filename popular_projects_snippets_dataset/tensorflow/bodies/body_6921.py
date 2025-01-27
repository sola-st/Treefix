# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
specs = []
worker_device_pairs = self._input_workers._worker_device_pairs  # pylint: disable=protected-access

for i, (input_device, compute_devices) in enumerate(worker_device_pairs):
    element_spec = nest.map_structure(
        functools.partial(_replace_per_replica_spec, i=i), self._element_spec)
    specs.append(
        _SingleWorkerDatasetIteratorSpec(input_device, compute_devices,
                                         element_spec, self._options,
                                         self._canonicalize_devices))
exit(specs)
