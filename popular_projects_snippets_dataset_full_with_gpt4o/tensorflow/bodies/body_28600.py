# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Generate 5 entries from iterator and save checkpoint.
outputs = self.gen_outputs(ds_fn, [], 5, verify_exhausted=False)
self.assertSequenceEqual(outputs, range(5))

# Restore from checkpoint and produce the rest of the elements from the
# iterator.
outputs.extend(
    self.gen_outputs(
        ds_fn, [],
        self.num_outputs - 5,
        ckpt_saved=True,
        verify_exhausted=False))
self.assertSequenceEqual(outputs, self.expected_outputs())
