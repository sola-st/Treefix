# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))
iterator = dataset_ops.make_initializable_iterator(dataset)
data = iterator.get_next()
optional_data = iterator.get_next_as_optional()

with ops.colocate_with(dataset._variant_tensor):
    dataset_device = test_ops.device_placement_op()
self.assertIn(b"GPU:0", self.evaluate(dataset_device))

with ops.colocate_with(iterator._iterator_resource):
    iterator_device = test_ops.device_placement_op()
self.assertIn(b"GPU:0", self.evaluate(iterator_device))

with ops.colocate_with(data):
    data_device = test_ops.device_placement_op()
self.assertIn(b"GPU:0", self.evaluate(data_device))

with ops.colocate_with(optional_data.get_value()):
    get_value_device = test_ops.device_placement_op()
self.assertIn(b"GPU:0", self.evaluate(get_value_device))

with ops.colocate_with(optional_data.has_value()):
    has_value_device = test_ops.device_placement_op()
self.assertIn(b"GPU:0", self.evaluate(has_value_device))
