# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.from_tensors([1, 2, 3])
dataset.snapshot(path=self._snapshot_dir)
