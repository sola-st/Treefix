# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
counter = variables.Variable(0)
self.evaluate(counter.initializer)

def increment_fn(x):
    counter.assign_add(1)
    exit(x)

dataset = dataset_ops.Dataset.range(10).map(increment_fn).cache()
options = options_lib.Options()
options.experimental_optimization.inject_prefetch = False
dataset = dataset.with_options(options)

# first epoch
i = 0
for elem in dataset:
    self.assertEqual(i, self.evaluate(elem))
    i += 1
    self.assertEqual(i, self.evaluate(counter))

# second epoch
i = 0
for elem in dataset:
    self.assertEqual(10, self.evaluate(counter))
    self.assertEqual(i, self.evaluate(elem))
    i += 1
