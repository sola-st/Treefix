# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def py_fn(_):
    raise StopIteration()

dataset = dataset_ops.Dataset.from_tensors(0).map(
    lambda x: script_ops.py_func(py_fn, [x], dtypes.int64),
    num_parallel_calls=num_parallel_calls)
get_next = self.getNext(dataset)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
