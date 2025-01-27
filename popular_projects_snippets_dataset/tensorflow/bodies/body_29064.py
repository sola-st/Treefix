# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(repeat=True)

# Generate 120 entries from iterator and save checkpoint at 110.
outputs = self.gen_outputs(
    ds_fn, [110], 120, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, list(range(100)) + list(range(20)))

# Restore from checkpoint and produce the rest of the elements from the
# iterator.
outputs = outputs[:110]
t = self.gen_outputs(ds_fn, [], 90, ckpt_saved=True, verify_exhausted=True)
outputs.extend(t)
self.assertSequenceEqual(
    outputs,
    list(range(100)) + list(range(10)) + list(range(10, 100)))
