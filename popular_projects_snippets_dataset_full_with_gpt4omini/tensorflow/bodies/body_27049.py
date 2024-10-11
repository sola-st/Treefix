# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/copy_to_device_test.py
host_dataset = dataset_ops.Dataset.range(10)
host_dataset = host_dataset.apply(testing.assert_next(["MapAndBatch"]))
host_dataset = host_dataset.map(lambda x: x*x).batch(10)
device_dataset = host_dataset.apply(
    prefetching_ops.copy_to_device("/cpu:1"))

with ops.device("/cpu:1"):
    iterator = dataset_ops.make_one_shot_iterator(device_dataset)
    next_element = iterator.get_next()

worker_config = config_pb2.ConfigProto(device_count={"CPU": 2})
with self.test_session(config=worker_config):
    self.assertAllEqual([x*x for x in range(10)], self.evaluate(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element)
