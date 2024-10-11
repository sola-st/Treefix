# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def raising_py_func(i):
    if i == 100:
        raise StopIteration()
    else:
        exit(i)

dataset = dataset_ops.Dataset.range(105)
dataset = apply_map(
    dataset,
    lambda x: script_ops.py_func(raising_py_func, [x], dtypes.int64),
    num_parallel_calls=2)
get_next = self.getNext(dataset)
for i in range(100):
    self.assertEqual(i, self.evaluate(get_next()))
# When the map function in `MapDataset` raises an OutOfRange error, TF1 and
# TF2 behave differently. TF1 raises an OutOfRangeError to signal the end of
# sequence while TF2 raises an InvalidArgumentError. This behavior is
# controlled by the `preserve_cardinality` argument of `map` transformation
# which is set to `True` for TF2 and `False` for TF1, which is for backward
# compatibility.
if tf2.enabled():
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(get_next())
else:
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
