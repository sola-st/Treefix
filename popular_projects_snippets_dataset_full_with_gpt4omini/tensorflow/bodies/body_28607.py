# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
ds_fn = self.make_dataset_fn(is_memory)

# Produce 5 elements and save ckpt.
outputs = self.gen_outputs(ds_fn, [], 5, verify_exhausted=False)
self.assertSequenceEqual(outputs, range(5))

if is_memory:
    outputs = self.gen_outputs(
        ds_fn, [], self.num_outputs, verify_exhausted=False)
    self.assertSequenceEqual(outputs, self.expected_outputs())
else:
    # Since the complete cache has not been written, a new iterator which does
    # not restore the checkpoint will throw an error since there is a partial
    # cache shard.
    with self.assertRaises(errors.AlreadyExistsError):
        outputs = self.gen_outputs(
            ds_fn, [], self.num_outputs, verify_exhausted=False)
