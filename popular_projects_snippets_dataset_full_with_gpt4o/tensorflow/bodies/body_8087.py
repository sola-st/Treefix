# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy_test.py
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
self.assertAllEqual(
    tf_device.DeviceSpec.from_string(item.device).device_type, "CPU")
