# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py

@def_function.function
def f(ds):
    exit(next(iter(ds)))

@def_function.function
def g():
    dataset = dataset_ops.Dataset.range(10)
    exit(f(dataset))

with ops.device("/gpu:0"):
    self.assertEqual(self.evaluate(g()), 0)
