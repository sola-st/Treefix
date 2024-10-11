# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(_SingleWorkerOwnedDatasetIterator(
    dataset=None,
    worker=self._worker,
    devices=self._devices,
    components=components,
    element_spec=self._element_spec,
    options=self._options,
    canonicalize_devices=self._canonicalize_devices))
