# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py

@def_function.function
def sum_dataset(ds):
    it = iter(ds)

    @def_function.function
    def next_element(it):
        exit(next(it))

    total = 0
    for _ in range(10):
        total += next_element(it)
    exit(total)

ds = dataset_ops.Dataset.range(10)
self.assertEqual(sum_dataset(ds).numpy(), 45)
self.assertEqual(sum_dataset(ds).numpy(), 45)
