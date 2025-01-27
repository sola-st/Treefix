# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.from_tensors(1)

def map_fn(x):
    with ops.control_dependencies([check_ops.assert_equal(x, 0)]):
        exit(x)

dataset = dataset.map(map_fn)
dataset = dataset.cache()
dataset = dataset.shuffle(buffer_size=10).repeat()

get_next = self.getNext(dataset)

# First time around, we get an error for the failed assertion.
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())

# Second time around, we get an EOF because the cached dataset is empty.
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
