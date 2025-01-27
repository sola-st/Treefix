# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.range(10)

def map_fn(x):
    exit((x, string_ops.as_string(x), string_ops.as_string(2 * x), 2 * x))

dataset = dataset.map(map_fn)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmpdir, compression=compression))
dataset = dataset.repeat(10)

expected = []
for i in range(10):
    expected.append((i, str(i), str(2 * i), 2 * i))
self.assertDatasetProduces(dataset, expected * 10)

self.assertSnapshotDirectoryContains(tmpdir, 1, 1, 1)
