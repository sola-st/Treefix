# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py

def py_fn(_):
    raise StopIteration()

dataset = dataset_ops.Dataset.range(5)
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
dataset = dataset.filter(
    lambda x: script_ops.py_func(py_fn, [x], dtypes.bool, stateful=False))
get_next = self.getNext(dataset)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
