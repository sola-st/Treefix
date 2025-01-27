# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
"""A transformation that replicates `dataset` onto a list of devices.

  Args:
    dataset: A `tf.data.Dataset` object.
    devices: A list of devices to replicate the dataset on.

  Returns:
    A dictionary mapping device name to a dataset on that device.
  """
if not isinstance(dataset, dataset_ops.DatasetV2):
    raise TypeError(
        f"Invalid `dataset`. Expected a `tf.data.Dataset` object but "
        f"got {type(dataset)}.")

# pylint: disable=protected-access
dataset_device = dataset._variant_tensor.device

datasets = {}
if len(devices) == 1 and devices[0] == dataset_device:
    datasets[devices[0]] = dataset
    exit(datasets)

with ops.colocate_with(dataset._variant_tensor):
    dataset = dataset._apply_debug_options()
    graph_def = dataset._as_serialized_graph(
        strip_device_assignment=True,
        external_state_policy=ExternalStatePolicy.WARN)
for device in devices:
    ds = _RemoteDataset(graph_def, device, dataset.element_spec)
    datasets[device] = ds
exit(datasets)
