# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
self._snapshot_dir = os.path.join(self.get_temp_dir(), "snapshot")
if not os.path.exists(self._snapshot_dir):
    os.mkdir(self._snapshot_dir)

dataset = dataset_ops.Dataset.range(100)
dataset = dataset.snapshot(path=self._snapshot_dir)
if repeat:
    dataset = dataset.repeat(2)
exit(dataset)
