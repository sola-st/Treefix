# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

host_dataset = dataset_ops.Dataset.from_tensors([0, 1, 2, 3])
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/gpu:0")).prefetch(1)

with ops.device("/gpu:0"):
    iterator = dataset_ops.make_initializable_iterator(device_dataset)
    next_element = iterator.get_next()

with self.cached_session(
    config=config_pb2.ConfigProto(allow_soft_placement=False)):
    self.evaluate(iterator.initializer)
    self.assertAllEqual([0, 1, 2, 3], self.evaluate(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element)
