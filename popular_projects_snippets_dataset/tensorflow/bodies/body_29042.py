# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, snapshot_name="my_custom_snapshot"))
dataset = dataset.repeat(10)
self.assertDatasetProduces(dataset, list(range(10)) * 10)

self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
self.assertTrue(
    os.path.exists(os.path.join(tmpdir, "custom-my_custom_snapshot")))
self.assertTrue(
    os.path.exists(
        os.path.join(tmpdir, "custom-my_custom_snapshot", "custom")))
