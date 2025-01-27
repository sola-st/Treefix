# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
ds1 = dataset_ops.Dataset.range(10).window(2)
ds2 = dataset_ops.Dataset.range(10, 20).window(2)
choice_dataset = dataset_ops.Dataset.range(2).repeat(5)
ds = dataset_ops.Dataset.choose_from_datasets([ds1, ds2], choice_dataset)
ds = ds.flat_map(lambda x: x)
expected = []
for i in range(5):
    for j in range(2):
        expected.extend([10*j + 2*i, 10*j + 2*i + 1])
self.assertDatasetProduces(ds, expected)
