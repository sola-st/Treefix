# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
ds_fn = self._build_snapshot_dataset(repeat=False)
outputs = self.gen_outputs(ds_fn, [], 50, verify_exhausted=False)
self.assertSequenceEqual(outputs, range(50))
outputs.extend(
    self.gen_outputs(ds_fn, [], 50, ckpt_saved=True, verify_exhausted=True))
self.assertSequenceEqual(outputs, range(100))
