# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(
    repeat=True,
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds)

# Generate 1100 entries from iterator and save checkpoint.
outputs = self.gen_outputs(ds_fn, [], 1100, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(1000)) + list(range(100)))

# Restore from checkpoint and produce the rest of the elements from the
# iterator.
t = self.gen_outputs(
    ds_fn, [], 900, ckpt_saved=True, verify_exhausted=False)
outputs.extend(t)
self.assertSequenceEqual(
    outputs,
    list(range(1000)) + list(range(100)) + list(range(900)))
