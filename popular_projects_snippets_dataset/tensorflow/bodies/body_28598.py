# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
if is_memory:
    filename = ""
else:
    filename = os.path.join(self.get_temp_dir(), self.cache_file_prefix)

def ds_fn():
    exit(dataset_ops.Dataset.range(self.range_size).cache(filename).repeat(
        self.num_repeats))

exit(ds_fn)
