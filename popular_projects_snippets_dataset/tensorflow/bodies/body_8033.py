# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, _ = self._get_test_object(
    task_type='worker', task_id=0, num_gpus=2)
input_options = distribute_lib.InputOptions(
    experimental_fetch_to_device=False)
dataset = dataset_ops.Dataset.range(100)
dataset = dataset.batch(distribution.num_replicas_in_sync)
dataset = distribution.experimental_distribute_dataset(
    dataset, options=input_options)
if isinstance(dataset, input_lib_v1.DistributedDatasetV1):
    item = dataset.make_initializable_iterator().get_next()
else:
    self.skipTest('unsupported test combination')
device_types = {
    tf_device.DeviceSpec.from_string(tensor.device).device_type for
    tensor in item.values}
self.assertAllEqual(list(device_types), ['CPU'])
