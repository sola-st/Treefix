# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_to_device_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

host_dataset = dataset_ops.Dataset.range(10)
device_dataset = host_dataset.apply(
    prefetching_ops.prefetch_to_device("/gpu:0"))

self.assertEqual(device_dataset._variant_tensor.device,
                 "/job:localhost/replica:0/task:0/device:GPU:0")
