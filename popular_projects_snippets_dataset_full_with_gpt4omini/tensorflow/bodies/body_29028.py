# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.from_tensors(42)
dataset = dataset.snapshot(path=self._snapshot_dir, name="snapshot")
self.assertDatasetProduces(dataset, [42])
