# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
fn = lambda _: random_ops.random_uniform((), seed=11)
dataset = apply_map(dataset, fn).repeat(1000).batch(10)

get_next = self.getNext(dataset)
random_values = self.evaluate(get_next())

# Assert that one of the next 99 batches yielded by the iterator is
# different from the first.
i = 0
while i < 99:
    if np.any(random_values != self.evaluate(get_next())):
        break
    i += 1
self.assertLess(i, 99)
