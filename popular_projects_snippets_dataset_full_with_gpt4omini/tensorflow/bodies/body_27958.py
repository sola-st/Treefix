# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))
iterator = iter(dataset)
data = next(iterator)
optional_data = iterator.get_next_as_optional()

self.assertIn("gpu:0", dataset._variant_tensor.device.lower())
self.assertIn("gpu:0", iterator._iterator_resource.device.lower())
self.assertIn("gpu:0", data.device.lower())
self.assertIn("gpu:0", optional_data.get_value().device.lower())
self.assertIn("gpu:0", optional_data.has_value().device.lower())
