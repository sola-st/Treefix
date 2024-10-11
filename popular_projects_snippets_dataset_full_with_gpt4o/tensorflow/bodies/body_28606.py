# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Produce 5 elements and checkpoint.
outputs = self.gen_outputs(ds_fn, [], 5, verify_exhausted=False)
self.assertSequenceEqual(outputs, range(5))

# Restore from checkpoint, then produce no elements and checkpoint.
outputs.extend(
    self.gen_outputs(ds_fn, [], 0, ckpt_saved=True, verify_exhausted=False))
self.assertSequenceEqual(outputs, range(5))

# Restore from checkpoint and produce rest of the elements.
outputs.extend(
    self.gen_outputs(
        ds_fn, [],
        self.num_outputs - 5,
        ckpt_saved=True,
        verify_exhausted=False))
self.assertSequenceEqual(outputs, list(range(10)) * 3)
