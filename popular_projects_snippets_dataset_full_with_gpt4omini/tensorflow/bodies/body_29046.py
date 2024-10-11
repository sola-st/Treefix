# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir
dataset = dataset_ops.Dataset.range(10)
with self.assertRaises(errors.NotFoundError):
    dataset = dataset.apply(snapshot.legacy_snapshot(tmpdir, mode="read"))
    get_next = self.getNext(dataset)
    self.evaluate(get_next())
