# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
"""Constructs a MultiDeviceIterator.

    Args:
      dataset: The input dataset to be iterated over.
      devices: The list of devices to fetch data to.
      max_buffer_size: Maximum size of the host side per device buffer to keep.
      prefetch_buffer_size: if > 0, then we setup a buffer on each device to
        prefetch into.
      source_device: The host device to place the `dataset` on.  In order to
        prevent deadlocks, if the prefetch_buffer_size is greater than the
        max_buffer_size, we set the max_buffer_size to prefetch_buffer_size.
    """
options = options_lib.Options()
options.experimental_distribute.num_devices = len(devices)
# If `prefetch_buffer_size` is 0, we turn off the `inject_prefetch`
# optimization to prevent potentially introducing asynchrony.
if prefetch_buffer_size == 0:
    options.experimental_optimization.inject_prefetch = False
dataset = dataset.with_options(options)
self._dataset = dataset._apply_debug_options()  # pylint: disable=protected-access
self._experimental_slack = dataset.options().experimental_slack
self._devices = devices
self._source_device = source_device
self._source_device_tensor = ops.convert_to_tensor(source_device)
self._max_buffer_size = max_buffer_size
self._prefetch_buffer_size = prefetch_buffer_size

if self._prefetch_buffer_size > self._max_buffer_size:
    self._max_buffer_size = self._prefetch_buffer_size

# Create the MultiDeviceIterator.
with ops.device(self._source_device):
    # TODO(b/121378567): Get rid of this shared_name hack.
    shared_name = ""
    if context.executing_eagerly():
        shared_name = context.anonymous_name()
    self._multi_device_iterator_resource = (
        gen_dataset_ops.multi_device_iterator(
            devices=self._devices,
            shared_name=shared_name,
            container="",
            **self._dataset._flat_structure))  # pylint: disable=protected-access
    if context.executing_eagerly():
        # Delete the resource when this object is deleted
        self._resource_deleter = resource_variable_ops.EagerResourceDeleter(
            handle=self._multi_device_iterator_resource,
            handle_device=self._source_device)

    # The incarnation ID is used to ensure consistency between the per-device
    # iterators and the multi-device iterator.
    self._incarnation_id = gen_dataset_ops.multi_device_iterator_init(
        self._dataset._variant_tensor,  # pylint: disable=protected-access
        self._multi_device_iterator_resource,
        max_buffer_size=self._max_buffer_size)

self._prototype_device_datasets = []
for i, device in enumerate(self._devices):
    with ops.device(device):
        ds = _PerDeviceGenerator(
            i,
            self._multi_device_iterator_resource,
            self._incarnation_id,
            self._source_device_tensor,
            self._dataset.element_spec,
            iterator_is_anonymous=False)
        self._prototype_device_datasets.append(ds)

    # TODO(rohanj): Explore the possibility of the MultiDeviceIterator to
    # initialize the device side of the pipeline. This would allow the
    # MultiDeviceIterator to choose, for example, to move some transformations
    # into the device side from its input. It might be useful in rewriting.
    # Create the per device iterators.
self._device_iterators = []
for i, device in enumerate(self._devices):
    with ops.device(device):
        ds = _create_device_dataset(self._prototype_device_datasets[i],
                                    self._incarnation_id,
                                    self._prefetch_buffer_size,
                                    self._experimental_slack)
        if context.executing_eagerly():
            self._device_iterators.append(dataset_ops.make_one_shot_iterator(ds))
        else:
            self._device_iterators.append(
                dataset_ops.make_initializable_iterator(ds))

if not context.executing_eagerly():
    device_iterator_initializers = [
        iterator.initializer for iterator in self._device_iterators
    ]
    self._initializer = control_flow_ops.group(*device_iterator_initializers)
