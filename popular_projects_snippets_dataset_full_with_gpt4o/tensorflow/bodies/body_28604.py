# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Generate 13 entries from iterator but save checkpoint after producing 5.
outputs = self.gen_outputs(
    ds_fn, [5], 13, verify_exhausted=False, save_checkpoint_at_end=False)
self.assertSequenceEqual(outputs, list(range(10)) + list(range(3)))

# Since we ran for more than one epoch, the cache was completely written.
# The ckpt was saved when the iterator was in cache-write mode. Test that
# the iterator falls back to read mode after restoring if the cache has
# been completely written.

outputs = list(range(5)) + self.gen_outputs(
    ds_fn, [],
    self.num_outputs - 5,
    ckpt_saved=True,
    verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) * 3)
