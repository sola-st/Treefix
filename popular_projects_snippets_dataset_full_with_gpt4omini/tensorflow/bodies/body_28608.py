# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Produce 15 elements and save ckpt. This will write the complete cache.
outputs = self.gen_outputs(ds_fn, [], 15, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) + list(range(5)))

# Build the iterator again but do not restore from ckpt. Since the cache
# has already been written we should be able to use it.
outputs = self.gen_outputs(
    ds_fn, [], self.num_outputs, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) * 3)
