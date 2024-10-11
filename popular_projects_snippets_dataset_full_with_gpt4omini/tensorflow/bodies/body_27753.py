# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
dataset = dataset_ops.Dataset.range(num_elements).take_while(
    lambda x: x < upper_bound)

self.assertDatasetProduces(dataset,
                           np.arange(min(num_elements, upper_bound)))
