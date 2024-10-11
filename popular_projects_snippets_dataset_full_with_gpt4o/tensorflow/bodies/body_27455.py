# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
if shuffle:
    actual = []
    next_fn = self.getNext(dataset)
    for _ in range(num_examples):
        elem = self.evaluate(next_fn())
        if isinstance(elem, tuple):
            actual.extend(elem)
        else:
            actual.extend(elem.tolist())

    self.assertCountEqual(actual, expected)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_fn())
else:
    self.assertDatasetProduces(dataset, list(chunk(expected, batch)))
