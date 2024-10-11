# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Create iterator for the `dataset` to fetch data to worker's `devices` .

    A `MultiDeviceIterator`  or `OwnedMultiDeviceIterator` is used to prefetch
    input to the devices on the given worker.

    Args:
      dataset: A `tf.data.Dataset` instance.
      worker: Worker on which ops should be created.
      devices: Distribute data from `dataset` to these devices.
      options: options.
    """
self._dataset = dataset
self._worker = worker
self._devices = devices
self._element_spec = dataset.element_spec
self._options = options
self._make_iterator()
