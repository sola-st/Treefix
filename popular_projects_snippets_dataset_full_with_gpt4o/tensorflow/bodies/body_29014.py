# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
dataset = dataset_ops.Dataset.range(1000)
with self.assertRaises(TypeError):
    dataset = dataset.snapshot(
        path=self._snapshot_dir, shard_func=lambda _: "invalid_fn")
    next_fn = self.getNext(dataset)
    self.evaluate(next_fn())
