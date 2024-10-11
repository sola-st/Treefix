# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(
    pending_snapshot_expiry_seconds=pending_snapshot_expiry_seconds)
outputs = self.gen_outputs(ds_fn, [], 100, verify_exhausted=False)
self.assertSequenceEqual(outputs, range(100))
outputs.extend(
    self.gen_outputs(
        ds_fn, [], 900, ckpt_saved=True, verify_exhausted=False))
self.assertSequenceEqual(outputs, range(1000))
