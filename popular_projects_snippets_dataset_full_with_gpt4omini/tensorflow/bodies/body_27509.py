# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/prefetch_to_device_test.py

if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))

self.assertIn("gpu:0", dataset._variant_tensor.device.lower())
