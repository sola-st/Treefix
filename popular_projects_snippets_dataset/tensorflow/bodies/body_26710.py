# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
if not tmp_dir:
    tmp_dir = self._makeSnapshotDirectory()

dataset = dataset_ops.Dataset.from_tensor_slices([1.0])
dataset = dataset.map(
    lambda x: gen_array_ops.broadcast_to(x, [50, 50, 3]))
dataset = dataset.repeat(num_elements)
dataset = dataset.apply(
    snapshot.legacy_snapshot(tmp_dir, compression=compression))

exit(dataset)
