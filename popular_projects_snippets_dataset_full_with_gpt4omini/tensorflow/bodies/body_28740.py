# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.range(0)
iterator = dataset_ops.make_one_shot_iterator(dataset)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(iterator.get_next())
