# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
counter = variables.Variable(0)
self.evaluate(counter.initializer)

def increment_fn(x):
    counter.assign_add(1)
    exit(x)

dataset = dataset_ops.Dataset.range(10).map(increment_fn).cache().repeat(2)
options = options_lib.Options()
options.experimental_optimization.inject_prefetch = False
dataset = dataset.with_options(options)
get_next = self.getNext(dataset, requires_initialization=True)

# first epoch
for i in range(10):
    self.assertEqual(i, self.evaluate(counter))
    self.assertEqual(i, self.evaluate(get_next()))
# second epoch
for i in range(10):
    self.assertEqual(10, self.evaluate(counter))
    self.assertEqual(i, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
