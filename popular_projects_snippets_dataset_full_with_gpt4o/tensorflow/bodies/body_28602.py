# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Generate 15 entries from iterator and save checkpoint.
outputs = self.gen_outputs(ds_fn, [], 15, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) + list(range(5)))

# Restore from checkpoint and produce the rest of the elements from the
# iterator.
outputs.extend(
    self.gen_outputs(
        ds_fn, [],
        self.num_outputs - 15,
        ckpt_saved=True,
        verify_exhausted=False))
self.assertSequenceEqual(outputs, self.expected_outputs())
