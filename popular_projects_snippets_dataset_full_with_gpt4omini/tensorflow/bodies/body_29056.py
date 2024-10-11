# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
tmpdir = self.snapshot_dir

dataset = dataset_ops.Dataset.from_tensor_slices([1.0])
dataset = dataset.map(lambda x: gen_array_ops.broadcast_to(x, [1024, 1024]))
dataset = dataset.repeat(10)
dataset = dataset.apply(
    snapshot.legacy_snapshot(
        tmpdir, shard_size_bytes=10 * 1024 * 1024, compression=compression))
next_fn = self.getNext(dataset)

for _ in range(10):
    self.evaluate(next_fn())

num_files = 1
if compression == snapshot.COMPRESSION_NONE:
    num_files = 3
self.assertSnapshotDirectoryContains(tmpdir, 1, 1, num_files)
