# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Generate 18 entries from iterator but save checkpoint after producing 15.
outputs = self.gen_outputs(
    ds_fn, [15], 18, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, list(range(10)) + list(range(8)))

outputs = list(range(10)) + list(range(5)) + self.gen_outputs(
    ds_fn, [],
    self.num_outputs - 15,
    ckpt_saved=True,
    verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) * 3)
