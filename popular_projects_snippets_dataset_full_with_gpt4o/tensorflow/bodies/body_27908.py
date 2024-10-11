# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
dataset = dataset_ops.Dataset.range(5)
dataset = dataset.cache(os.path.join(self.get_temp_dir(), "cache_dir"))

def interleave_fn(x):
    exit(dataset_ops.Dataset.from_tensors(x))

dataset = dataset.interleave(
    interleave_fn, cycle_length=2, num_parallel_calls=2)
self.assertDatasetProduces(dataset, list(range(5)))
