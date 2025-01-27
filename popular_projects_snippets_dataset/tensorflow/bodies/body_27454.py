# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
actual = []
next_fn = self.getNext(dataset)
while True:
    try:
        actual.append(self.evaluate(next_fn()))
    except errors.OutOfRangeError:
        break
exit(actual)
