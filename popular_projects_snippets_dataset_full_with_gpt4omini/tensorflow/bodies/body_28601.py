# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Generate 8 entries from iterator but save checkpoint after producing 5.
outputs = self.gen_outputs(
    ds_fn, [5], 8, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, range(8))

outputs = outputs[:5]
outputs.extend(
    self.gen_outputs(
        ds_fn, [],
        self.num_outputs - 5,
        ckpt_saved=True,
        verify_exhausted=False))
self.assertSequenceEqual(outputs, self.expected_outputs())
