# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
input_options = distribute_lib.InputOptions(
    experimental_fetch_to_device=False)
dataset = dataset_ops.Dataset.range(100)
dataset = dataset.batch(distribution.num_replicas_in_sync)
dataset = distribution.experimental_distribute_dataset(
    dataset, options=input_options)
if context.executing_eagerly():
    item = next(iter(dataset))
else:
    if isinstance(dataset, input_lib_v1.DistributedDatasetV1):
        item = dataset.make_initializable_iterator().get_next()
    else:
        self.skipTest("unsupported test combination")
device_types = {
    tf_device.DeviceSpec.from_string(tensor.device).device_type for
    tensor in item.values}
self.assertAllEqual(list(device_types), ["CPU"])
