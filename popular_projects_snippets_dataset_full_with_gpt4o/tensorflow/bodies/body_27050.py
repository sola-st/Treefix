# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
host_dataset = dataset_ops.Dataset.from_tensors([0, 1, 2, 3])
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/cpu:1"))

with ops.device("/cpu:1"):
    iterator = dataset_ops.make_one_shot_iterator(device_dataset)
    next_element = iterator.get_next()

self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(host_dataset),
        dataset_ops.get_structure(device_dataset)))

self.assertEqual(dtypes.int32, next_element.dtype)
self.assertEqual((4,), next_element.shape)

worker_config = config_pb2.ConfigProto(device_count={"CPU": 2})
with self.test_session(config=worker_config):
    self.assertAllEqual([0, 1, 2, 3], self.evaluate(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element)
