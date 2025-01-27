# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds)

# Generate 200 entries from iterator but save checkpoint after producing
# 100.
outputs = self.gen_outputs(
    ds_fn, [100], 200, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, range(200))

outputs = outputs[:100]
outputs.extend(
    self.gen_outputs(
        ds_fn, [], 900, ckpt_saved=True, verify_exhausted=False))
self.assertSequenceEqual(outputs, range(1000))
