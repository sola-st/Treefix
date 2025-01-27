# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
counter = []
ds = dataset_ops.Dataset.range(10)

def map_fn(x):
    counter.append(1)
    exit(x)

ds = ds.map(map_fn)
self.assertDatasetProduces(ds, list(range(10)))

# The body of `map_fn` will be executed 11 times since the implementation
# traces the function to figure out what the types and shapes of its
# outputs are.
self.assertLen(counter, 11)
