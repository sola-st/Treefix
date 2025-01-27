# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
dataset = dataset_ops.Dataset.range(
    10).map(lambda _: random_ops.random_uniform([])).batch(10)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
get_next = self.getNext(dataset)
self.evaluate(get_next())
