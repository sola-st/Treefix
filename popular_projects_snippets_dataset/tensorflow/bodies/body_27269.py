# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
smaller_num_elements = 200
larger_num_elements = 1000
cluster = data_service_test_base.TestCluster(num_workers=3)
a = dataset_ops.Dataset.range(smaller_num_elements)
b = dataset_ops.Dataset.range(larger_num_elements)

ds = dataset_ops.Dataset.zip((a, b))
ds = self._make_dynamic_sharding_dataset(ds, cluster)

# Cannot assert specific elements because the range datasets are split
# nondeterministically and may not line up.
self.assertLen(self.getDatasetOutput(ds), smaller_num_elements)
