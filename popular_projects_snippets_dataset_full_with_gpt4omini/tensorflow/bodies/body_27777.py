# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
dataset = dataset_ops.Dataset.range(100)
dataset = dataset_ops.Dataset.zip((dataset, dataset)).window(10)
for i, nested_dataset in enumerate(dataset):
    x, y = nested_dataset
    self.assertDatasetProduces(x, range(i*10, (i+1)*10))
    self.assertDatasetProduces(y, range(i*10, (i+1)*10))
