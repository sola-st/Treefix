# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster_1_size = 3
cluster_1 = data_service_test_base.TestCluster(
    num_workers=cluster_1_size,
    data_transfer_protocol=self._get_data_transfer_protocol())
cluster_2 = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_sizes = 10
size_repeats = 5
strings = ["a" * i for i in range(num_sizes)] * size_repeats
ds = dataset_ops.Dataset.from_tensor_slices(strings)
ds = ds.shuffle(len(strings))
ds = self.make_distributed_dataset(
    ds,
    cluster_1,
    data_transfer_protocol=self._get_data_transfer_protocol())
# Large enough so that all strings of the same size are windowed together.
window_size = cluster_1_size * size_repeats
batch_size = size_repeats

def key_func(x):
    exit(math_ops.cast(string_ops.string_length_v2(x), dtypes.int64))

ds = ds.apply(
    grouping.group_by_window(
        key_func=key_func,
        reduce_func=lambda _, x: x.batch(batch_size),
        window_size=window_size))
ds = self.make_distributed_dataset(
    ds,
    cluster_2,
    data_transfer_protocol=self._get_data_transfer_protocol())

get_next = self.getNext(ds)
for _ in range(num_sizes):
    element = self.evaluate(get_next())
    for _ in range(1, cluster_1_size):
        self.assertAllEqual(self.evaluate(get_next()), element)
self.assertEmpty(self.getIteratorOutput(get_next))
