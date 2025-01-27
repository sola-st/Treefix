# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

host_dataset = dataset_ops.Dataset.range(10)
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/gpu:0")).prefetch(1)

with ops.device("/gpu:0"):
    self.assertDatasetProduces(device_dataset, list(range(10)))
