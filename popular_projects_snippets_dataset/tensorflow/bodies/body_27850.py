# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
exit(dataset_ops.Dataset.range(10).map(self._sparse).batch(batch_size))
