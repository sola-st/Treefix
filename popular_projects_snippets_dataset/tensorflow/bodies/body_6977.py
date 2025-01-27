# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Create iterator for the `dataset` to fetch data to worker's `devices` .

    `OwnedMultiDeviceIterator` is used to prefetch input to the devices on the
    given worker. The lifetime of this iterator is tied to the encompassing
    python object. Once we go out of scope of the python object or return from
    a tf.function the underlying iterator resource is deleted.

    Args:
      dataset: A `tf.data.Dataset` instance.
      worker: Worker on which ops should be created.
      devices: Distribute data from `dataset` to these devices.
      components: Tensor components to construct the
        _SingleWorkerOwnedDatasetIterator from.
      element_spec: A nested structure of `TypeSpec` objects that represents the
      type specification of elements of the iterator.
      options: `tf.distribute.InputOptions` used to control options on how this
      dataset is distributed.
      canonicalize_devices: Whether to canonicalize devices for workers fully or
      partially. If False, it will partially canonicalize devices by removing
      job and task.
    """
if worker is None or devices is None:
    raise ValueError("Both `worker` and `devices` should be provided")

error_message = ("Either `dataset` or both `components` and `element_spec` "
                 "need to be provided.")

self._options = options
self._canonicalize_devices = canonicalize_devices
if dataset is None:
    if (components is None or element_spec is None):
        raise ValueError(error_message)
    self._element_spec = element_spec
    self._worker = worker
    self._devices = devices
    self._iterator = components[0]
else:
    if (components is not None or element_spec is not None):
        raise ValueError(error_message)
    super(_SingleWorkerOwnedDatasetIterator,
          self).__init__(dataset, worker, devices, self._options)
