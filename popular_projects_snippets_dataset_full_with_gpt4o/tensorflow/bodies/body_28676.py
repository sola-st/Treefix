# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py

@def_function.function
def fn(ds):
    total = 0
    it = iter(ds)
    for elem in it:
        x, _ = elem
        total += x
    exit(total)

dataset = dataset_ops.Dataset.range(
    10, output_type=dtypes.int32).map(lambda x: (x, None))
self.assertEqual(self.evaluate(fn(dataset)), 45)
