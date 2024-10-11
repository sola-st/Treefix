# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset1 = dataset_ops.Dataset.range(1000)
dataset1 = dataset1.snapshot(path=self._snapshot_dir)
next1 = self.getNext(dataset1)
for i in range(500):
    self.assertEqual(i, self.evaluate(next1()))

dataset2 = dataset_ops.Dataset.range(1000)
dataset2 = dataset2.snapshot(path=self._snapshot_dir)
next2 = self.getNext(dataset2)
for i in range(500):
    self.assertEqual(i, self.evaluate(next2()))

for i in range(500, 1000):
    self.assertEqual(i, self.evaluate(next1()))
    self.assertEqual(i, self.evaluate(next2()))

self.assertSnapshotDirectoryContains(
    self._snapshot_dir,
    num_fingerprints=1,
    num_runs_per_fingerprint=2,
    num_snapshot_shards_per_run=multiprocessing.cpu_count())
