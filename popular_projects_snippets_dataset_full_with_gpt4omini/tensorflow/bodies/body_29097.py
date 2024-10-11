# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
ds = dataset_ops.Dataset.from_tensors(0)
result = ds

for _ in range(99):
    result = result.concatenate(ds)
self.assertDatasetProduces(result, [0]*100)
