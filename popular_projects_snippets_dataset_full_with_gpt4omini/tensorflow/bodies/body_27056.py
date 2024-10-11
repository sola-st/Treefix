# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py

def make_tensor(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0, 0]], values=(i * [1]), dense_shape=[2, 2]))

host_dataset = dataset_ops.Dataset.range(10).map(make_tensor)

device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/cpu:1"))

with ops.device("/cpu:1"):
    iterator = dataset_ops.make_one_shot_iterator(device_dataset)
    next_element = iterator.get_next()

self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(host_dataset),
        dataset_ops.get_structure(device_dataset)))

self.assertEqual(dtypes.int64, next_element.dtype)

worker_config = config_pb2.ConfigProto(device_count={"CPU": 2})
with self.test_session(config=worker_config):
    for i in range(10):
        actual = self.evaluate(next_element)
        self.assertAllEqual([i], actual.values)
        self.assertAllEqual([[0, 0]], actual.indices)
        self.assertAllEqual([2, 2], actual.dense_shape)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element)
