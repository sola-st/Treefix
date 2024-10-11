# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(repeat=False)
outputs = self.gen_outputs(
    ds_fn, [10], 20, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, range(20))

outputs = outputs[:10]
outputs.extend(
    self.gen_outputs(ds_fn, [], 90, ckpt_saved=True, verify_exhausted=True))
self.assertSequenceEqual(outputs, range(100))
