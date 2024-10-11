# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(repeat=True)

# Generate 50 entries from iterator and save checkpoint.
outputs = self.gen_outputs(ds_fn, [], 50, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(50)))

# Restore from checkpoint and produce the rest of the elements from the
# iterator.
t = self.gen_outputs(
    ds_fn, [], 150, ckpt_saved=True, verify_exhausted=False)
outputs.extend(t)
self.assertSequenceEqual(
    outputs,
    list(range(50)) + list(range(50, 100)) + list(range(100)))
