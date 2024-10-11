# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([42],
                                                 name="from_tensor_slices")
self.assertDatasetProduces(dataset, [42])
