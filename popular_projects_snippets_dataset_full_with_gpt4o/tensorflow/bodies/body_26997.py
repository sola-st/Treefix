# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def raising_py_fn(i):
    if i >= threshold:
        raise StopIteration()
    else:
        exit(i)

dataset = dataset_ops.Dataset.range(100).apply(
    batching.map_and_batch(
        lambda x: script_ops.py_func(raising_py_fn, [x], dtypes.int64),
        batch_size=10))

get_next = self.getNext(dataset)
for i in range(threshold // 10):
    self.assertAllEqual([i * 10 + j for j in range(10)],
                        self.evaluate(get_next()))
for i in range(threshold // 10, 10):
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
