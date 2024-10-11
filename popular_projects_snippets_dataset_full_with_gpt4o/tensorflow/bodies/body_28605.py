# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Checkpoint before get_next is called even once.
outputs = self.gen_outputs(ds_fn, [], 0, verify_exhausted=False)
self.assertSequenceEqual(outputs, [])

outputs = self.gen_outputs(
    ds_fn, [], self.num_outputs, ckpt_saved=True, verify_exhausted=False)
self.assertSequenceEqual(outputs, list(range(10)) * 3)
