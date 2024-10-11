# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
"""Constructs an owned MultiDeviceIterator object.

    Args:
      dataset: The input dataset to be iterated over.
      devices: (Required.) The list of devices to fetch data to.
      max_buffer_size: Maximum size of the host side per device buffer to keep.
      prefetch_buffer_size: if > 0, then we setup a buffer on each device to
        prefetch into.
      source_device: The host device to place the `dataset` on.  In order to
        prevent deadlocks, if the prefetch_buffer_size is greater than the
        max_buffer_size, we set the max_buffer_size to prefetch_buffer_size.
      components: Tensor components to construct the MultiDeviceIterator from.
      element_spec: A (nested) structure of `tf.TypeSpec` objects that
        represents the type specification of elements of the iterator.

    Raises:
      RuntimeError: If executed in graph mode or outside of function building
        mode.
      ValueError: If any of the following happens:
        - `devices` is `None`
        - `dataset` is `None` and either `components` or `element_spec` is
          `None`
        - `dataset` is not None and either `components` or `element_spec` is
          provided
    """
if not context.executing_eagerly() and not ops.inside_function():
    raise RuntimeError("OwnedMultiDeviceIterator is only supported inside of "
                       "tf.function or when eager execution is enabled.")
if devices is None:
    raise ValueError("`devices` must be provided.")

if dataset is None:
    if (components is None or element_spec is None):
        raise ValueError(
            "When `dataset` is not provided, both `components` and "
            "`element_spec` must be specified.")
    self._element_spec = element_spec
    self._devices = devices
    self._source_device = source_device
    self._multi_device_iterator_resource = components[0]
    self._device_iterators = components[1:]
else:
    if (components is not None or element_spec is not None):
        raise ValueError(
            "When `dataset` is provided, `element_spec` and `components` must "
            "not be specified.")
    options = options_lib.Options()
    options.experimental_distribute.num_devices = len(devices)
    # If `prefetch_buffer_size` is 0, we turn off the `inject_prefetch`
    # optimization to prevent potentially introducing asynchrony.
    if prefetch_buffer_size == 0:
        options.experimental_optimization.inject_prefetch = False
    dataset = dataset.with_options(options)
    dataset = dataset._apply_debug_options()  # pylint: disable=protected-access
    self._element_spec = dataset.element_spec
    experimental_slack = dataset.options().experimental_slack
    self._devices = devices
    self._source_device = source_device
    source_device_tensor = ops.convert_to_tensor(self._source_device)

    if prefetch_buffer_size > max_buffer_size:
        max_buffer_size = prefetch_buffer_size

    # Create the MultiDeviceIterator.
    with ops.device(self._source_device):
        self._multi_device_iterator_resource = (
            gen_dataset_ops.anonymous_multi_device_iterator_v3(
                devices=self._devices, **dataset._flat_structure))  # pylint: disable=protected-access

        # The incarnation ID is used to ensure consistency between the
        # per-device iterators and the multi-device iterator.
        incarnation_id = gen_dataset_ops.multi_device_iterator_init(
            dataset._variant_tensor,  # pylint: disable=protected-access
            self._multi_device_iterator_resource,
            max_buffer_size=max_buffer_size)

    prototype_device_datasets = []
    for i, device in enumerate(self._devices):
        with ops.device(device):
            ds = _PerDeviceGenerator(
                i,
                self._multi_device_iterator_resource,
                incarnation_id,
                source_device_tensor,
                dataset.element_spec,
                iterator_is_anonymous=True,
            )
            prototype_device_datasets.append(ds)

      # TODO(rohanj): Explore the possibility of the MultiDeviceIterator to
      # initialize the device side of the pipeline. This would allow the
      # MultiDeviceIterator to choose, for example, to move some transformations
      # into the device side from its input. It might be useful in rewriting.
      # Create the per device iterators.
    self._device_iterators = []

    for i, device in enumerate(self._devices):
        with ops.device(device):
            ds = _create_device_dataset(prototype_device_datasets[i],
                                        incarnation_id, prefetch_buffer_size,
                                        experimental_slack)
            iterator = iter(ds)
            self._device_iterators.append(iterator)
