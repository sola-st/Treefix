# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
words = [b"foo", b"bar", b"baz"]
datasets = [dataset_ops.Dataset.from_tensors(w).repeat() for w in words]
choice_array = np.random.randint(3, size=(15,), dtype=np.int64)
choice_dataset = dataset_ops.Dataset.from_tensor_slices(choice_array)
ds = dataset_ops.Dataset.choose_from_datasets(datasets, choice_dataset)
ds = self._make_dynamic_sharding_dataset(ds, cluster)
expected = [words[i] for i in choice_array] * num_workers

assert_items_equal = (num_workers > 1)
self.assertDatasetProduces(
    ds, expected, assert_items_equal=assert_items_equal)
