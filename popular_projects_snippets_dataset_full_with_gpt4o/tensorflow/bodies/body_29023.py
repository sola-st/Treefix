# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.range(1000)
dataset = dataset.shuffle(1000)
dataset = dataset.snapshot(path=self._snapshot_dir)
exit(dataset)
