# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
random_seed.set_random_seed(None)
num_elements = 100
cluster = data_service_test_base.TestCluster(
    num_workers=2,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.range(num_elements)
ds = ds.shuffle(num_elements, seed=shuffle_seed)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
output = self.getDatasetOutput(ds)

# The output will be two sequences of range(num_elements)
# non-deterministically interleaved together. If the orders of the elements
# were the same, first_order and second_order computed below will be equal.
first_order = {}
second_order = {}
for element in output:
    if element in first_order:
        second_order[element] = len(second_order)
    else:
        first_order[element] = len(first_order)
if shuffle_seed is None:
    self.assertNotEqual(first_order, second_order)
else:
    self.assertEqual(first_order, second_order)
