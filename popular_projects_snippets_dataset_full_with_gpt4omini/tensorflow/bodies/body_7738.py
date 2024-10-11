# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()
dataset = dataset_ops.Dataset.range(
    strategy.num_replicas_in_sync * 2,
    output_type=dtypes.float32).batch(strategy.num_replicas_in_sync)

# Check default, should prefetch to TPU.
dataset_item = next(iter(strategy.experimental_distribute_dataset(dataset)))
dataset_location = tf_device.DeviceSpec.from_string(
    dataset_item.values[0].device)
self.assertEqual(dataset_location.device_type, "TPU")
