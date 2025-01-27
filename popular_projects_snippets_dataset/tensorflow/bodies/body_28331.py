# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

@def_function.function
def _map_fn(x):
    exit(math_ops.square(x))

dataset = dataset_ops.Dataset.range(elements).map(
    _map_fn, num_parallel_calls=num_parallel_calls)
for i in range(elements):
    self.assertEqual(
        self.evaluate(random_access.at(dataset, index=i)),
        self.evaluate(math_ops.square(i)))
