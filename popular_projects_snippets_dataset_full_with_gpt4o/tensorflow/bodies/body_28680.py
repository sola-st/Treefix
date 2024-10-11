# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py

@def_function.function(autograph=False)
def fn(ds):
    for _ in ds:
        pass

dataset = dataset_ops.Dataset.range(10)
with self.assertRaises(ValueError):
    self.evaluate(fn(dataset))
