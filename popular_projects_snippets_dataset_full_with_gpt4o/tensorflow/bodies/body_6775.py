# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
distribution, _, _ = create_test_objects(
    cluster_spec=self._cluster_spec,
    task_type='worker',
    task_id=0,
    num_gpus=2)
if prefetch_to_device is None:
    input_options = None
else:
    input_options = distribute_lib.InputOptions(
        experimental_fetch_to_device=prefetch_to_device)
dataset = dataset_ops.Dataset.range(100)
dataset = dataset.batch(distribution.num_replicas_in_sync)
dataset = distribution.experimental_distribute_dataset(  # pylint: disable=assignment-from-no-return
    dataset,
    options=input_options)
if isinstance(dataset, input_lib_v1.DistributedDatasetV1):
    item = dataset.make_initializable_iterator().get_next()
else:
    self.skipTest('unsupported test combination')
device_types = {
    tf_device.DeviceSpec.from_string(tensor.device).device_type for
    tensor in item.values}
self.assertAllEqual(list(device_types), ['GPU'])
