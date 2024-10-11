# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
input_datasets = (dataset_ops.Dataset.range(0),
                  (dataset_ops.Dataset.range(1),
                   dataset_ops.Dataset.range(2)))
self._testVariadicInputs(dataset_ops.Dataset.zip, input_datasets)
