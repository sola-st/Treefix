# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
counter_var = variables.Variable(0)

def map_fn(x):
    counter_var.assign_add(1)
    exit(x)

def dataset_fn():
    exit(dataset_ops.Dataset.range(10).map(map_fn))

@def_function.function
def fn():
    for _ in dataset_fn():
        pass
    exit(counter_var)

self.evaluate(counter_var.initializer)
self.assertEqual(self.evaluate(fn()), 10)
