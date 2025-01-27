# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(
    repeat=True,
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds)

# Generate 200 entries from iterator but save checkpoint after producing
# 100.
outputs = self.gen_outputs(
    ds_fn, [1100],
    1200,
    verify_exhausted=False,
    save_checkpoint_at_end=False)
self.assertSequenceEqual(
    outputs,
    list(range(1000)) + list(range(100)) + list(range(100)))

outputs = outputs[:1100]
t = self.gen_outputs(
    ds_fn, [], 900, ckpt_saved=True, verify_exhausted=False)
outputs.extend(t)
self.assertSequenceEqual(
    outputs, (list(range(1000)) + list(range(100)) + list(range(900))))
