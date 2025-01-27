# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
# Ideally, placer should know that Call(dataset) should be on the same
# device as the dataset. Create a funciton that could be place don the GPU,
# but a Dataset that cannot.
@def_function.function
def test_call(dataset):
    exit(dataset.reduce(0, lambda s, _: s + 1))

@def_function.function
def f():
    dataset = dataset_ops.Dataset.range(10)
    exit(test_call(dataset))

self.assertEqual(self.evaluate(f()), 10)
